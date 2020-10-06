#include <bits/stdc++.h>
using namespace std;

#define KBYTES 1024
#define BLOCKS (64*KBYTES)

#define byte	unsigned char
#define word16	unsigned short int
#define word32	unsigned long int

#define burn(x)	memset( x, 0, sizeof( x ) )

#define IDEAKEYSIZE	16
#define IDEABLOCKSIZE	8

#define IDEAROUNDS	8
#define IDEAKEYLEN	( 6 * IDEAROUNDS + 4 )

typedef word16 uint16;
#define low16(x) ((x) & 0xFFFF)

/*
 * MUL(x,y) computes x = x*y, modulo 0x10001.  Requires two temps, 
 * t16 and t32.  x is modified, and must me a side-effect-free lvalue.
 * y may be anything, but unlike x, must be strictly 16 bits.
 */

#define MUL(x,y) \
	((t16 = (y)) ? \
		(x=low16(x)) ? \
			t32 = (word32)x*t16, \
			x = low16(t32), \
			t16 = t32>>16, \
			x = (x-t16)+(x<t16) \
		: \
			(x = 1-t16) \
	: \
		(x = 1-x))

/*
 * Compute the multiplicative inverse of x, modulo 65537, using Euclid's
 * algorithm. It is unrolled twice to avoid swapping the registers each
 * iteration, and some subtracts of t have been changed to adds.
 */
const static uint16 mulInv(uint16 x)     
{
	uint16 t0, t1;
	uint16 q, y;

	if (x <= 1)
		return x;	/* 0 and 1 are self-inverse */
	t1 = 0x10001L / x;	/* Since x >= 2, this fits into 16 bits */
	y = 0x10001L % x;
	if (y == 1)
		return low16(1-t1);
	t0 = 1;
	do {
		q = x / y;
		x = x % y;
		t0 += q * t1;
		if (x == 1)
			return t0;
		q = y / x;
		y = y % x;
		t1 += q * t0;
	} while (y != 1);
	return low16(1-t1);
} /* mukInv */

/*
 * Expand a 128-bit user key to a working encryption key EK
 */
void ideaExpandKey(byte const *userkey, word16 *EK)
{
	int i,j;

	for (j=0; j<8; j++) {
		EK[j] = (userkey[0]<<8) + userkey[1];
		userkey += 2;
	}
	for (i=0; j < IDEAKEYLEN; j++) {
		i++;
		EK[i+7] = (EK[i & 7] << 9) | (EK[i+1 & 7] >> 7);
		EK += i & 8;
		i &= 7;
	}
} /* ideaExpandKey */

/*
 * Compute IDEA decryption key DK from an expanded IDEA encryption key EK
 * Note that the input and output may be the same.  Thus, the key is
 * inverted into an internal buffer, and then copied to the output.
 */
void ideaInvertKey(word16 const *EK, word16 DK[IDEAKEYLEN])
{
	int i;
	uint16 t1, t2, t3;
	word16 temp[IDEAKEYLEN];
	word16 *p = temp + IDEAKEYLEN;

	t1 = mulInv(*EK++);
	t2 = -*EK++;
	t3 = -*EK++;
	*--p = mulInv(*EK++);
	*--p = t3;
	*--p = t2;
	*--p = t1;

	for (i = 0; i < IDEAROUNDS-1; i++) {
		t1 = *EK++;
		*--p = *EK++;
		*--p = t1;

		t1 = mulInv(*EK++);
		t2 = -*EK++;
		t3 = -*EK++;
		*--p = mulInv(*EK++);
		*--p = t2;
		*--p = t3;
		*--p = t1;
	}
	t1 = *EK++;
	*--p = *EK++;
	*--p = t1;

	t1 = mulInv(*EK++);
	t2 = -*EK++;
	t3 = -*EK++;
	*--p = mulInv(*EK++);
	*--p = t3;
	*--p = t2;
	*--p = t1;
/* Copy and destroy temp copy */
	memcpy(DK, temp, sizeof(temp));
	burn(temp);
} /* ideaInvertKey */

/*	IDEA encryption/decryption algorithm */
/* Note that in and out can be the same buffer */
void decrypt(byte const (inbuf[8]), byte (outbuf[8]), word16 const *key)
{
	register uint16 x1, x2, x3, x4, s2, s3;
	word16 *in, *out;
	register uint16 t16;	/* Temporaries needed by MUL macro */
	register word32 t32;
	int r = IDEAROUNDS;

	in = (word16 *)inbuf;
	x1 = *in++;  x2 = *in++;
	x3 = *in++;  x4 = *in;
	x1 = (x1>>8) | (x1<<8);
	x2 = (x2>>8) | (x2<<8);
	x3 = (x3>>8) | (x3<<8);
	x4 = (x4>>8) | (x4<<8);
	do {
		MUL(x1,*key++);
		x2 += *key++;
		x3 += *key++;
		MUL(x4, *key++);

		s3 = x3;
		x3 ^= x1;
		MUL(x3, *key++);
		s2 = x2;
		x2 ^= x4;
		x2 += x3;
		MUL(x2, *key++);
		x3 += x2;

		x1 ^= x2;  x4 ^= x3;

		x2 ^= s3;  x3 ^= s2;
	} while (--r);
	MUL(x1, *key++);
	x3 += *key++;
	x2 += *key++;
	MUL(x4, *key);

	out = (word16 *)outbuf;
	x1 = low16(x1);
	x2 = low16(x2);
	x3 = low16(x3);
	x4 = low16(x4);
	*out++ = (x1>>8) | (x1<<8);
	*out++ = (x3>>8) | (x3<<8);
	*out++ = (x2>>8) | (x2<<8);
	*out   = (x4>>8) | (x4<<8);
// #endif
} /* ideaCipher */

int main()
{	
	byte userkey[16];
	word16 EK[IDEAKEYLEN], DK[IDEAKEYLEN];
	byte decrypted_arr[8];

	ifstream myfile("key.txt");
	string line;
	int counter = 0;
	while(getline(myfile, line))
		userkey[counter++] = stoi(line);

	ideaExpandKey(userkey, EK);
	ideaInvertKey(EK, DK);

	string decrypted_text = "";
	int len;
	cin >> len;
	int add = (8 - (len % 8)) % 8;
	int new_len = len + add;
	int iter = new_len / 8;

	vector<int>ciphertext(new_len);
	for(int i=0;i<new_len;i++) cin >> ciphertext[i];

	for(int i=0;i<iter;i++)
	{	
		for (int k=0; k<8; k++) 
			decrypted_arr[k] = (byte)ciphertext[i * 8 + k];
		for (long l = 0; l < BLOCKS; l++)
			decrypt(decrypted_arr, decrypted_arr, DK);
		
		for(int k=0;k<8;k++)
			decrypted_text += decrypted_arr[k];
	}
	string original_text = "";
	for(int i=0;i<len;i++) original_text += decrypted_text[i];
	cout << original_text << endl;
	return 0;
}
