

# Algorithm Explanation

Given a plaintext, a key is chosen and the key is made to cyclically repeat itself till the length of key is equal to length of plaintext.
Ex - If plaintext is heythere and key is cat, then the key would be cyclically repeated till it has length 8.
So final key would be catcatca

Each character of the plaintext and key is assumed to be in lowercase alphabets.

Now, each character from a - z is mapped to their alphabetical order from 0 - 25.

Let m[] be the mapping vector converting character to its alphabetical order. Ex - m[a] = 0, m[z] = 25

Ciphertext[i] = (m[Plaintext[i]] + m[key[i]]) % 26

To get the character at position i of ciphertext, mapping of plaintext at position i and key at position i is added modulo 26.
The final number is converted back to the corresponding alphabetical character by reverse mapping.

Ex - Plaintext -> heythere  
     Key ->       catcatca  
     Ciphetext -> jervhxte  

# Problem Statement

Given an enrypted message, find the plaintext.
Encrypted Message = "vvkkwikrotorvsikrphbkptsrtoavjmhikroto"

# Access
You can look at the code but you do not have access to encryption or decryption server.

# Solution
To find the length of the key, we see repeating substrings in the ciphertext, these denote that some substring from the plaintext is encoded again using the same portion of key at these two positions. Let the First occurence of the most frequently occuring substring be at x and second occurence be at y. Then y - x would be a multiple of key length. We do this process for all pair of occurences of the most frequently occuring substring (we consider only substrings of length >= 3) and the key length would be the gcd of all these differences of indices.

Here, we can see that most frequently occuring substring of length >= 3 is "ikr" and gcd of difference of positions of its occurences is 9.
So key length is 9.

Once we have the length of key, we can see that if we consider characters of ciphertext at positions 1, key_length + 1, 2 * key_length + 1, ...., they form a simple caeser cipher which could be solved using frequency analysis.

Algorithm to find plaintext -> Make groups of all positions of ciphertext mod key_length. For each string, use frequency anaylsis to brek the caeser cipher and get the characters at the positions.

Plaintext = "catchthecatandthedogthedogchasesthecat"
