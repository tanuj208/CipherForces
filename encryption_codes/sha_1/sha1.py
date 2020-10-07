import struct

def ini_variables():
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    return h0, h1, h2, h3, h4

def format_message(message):
     # Pre-processing:
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8
    
    # append the bit '1' to the message
    message += b'\x80'
    
    # append 0 <= k < 512 bits '0', so that the resulting message length (in bits)
    #    is congruent to 448 (mod 512)
    message += b'\x00' * ((56 - (original_byte_len + 1) % 64) % 64)
    
    # append length of message (before pre-processing), in bits, as 64-bit big-endian integer
    message += struct.pack(b'>Q', original_bit_len)

    return message

def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

def process_chunk(h0, h1, h2, h3, h4, w):
    a = h0
    b = h1
    c = h2
    d = h3
    e = h4

    for i in range(80):
        if 0 <= i <= 19:
            f = d ^ (b & (c ^ d))
            k = 0x5A827999
        elif 20 <= i <= 39:
            f = b ^ c ^ d
            k = 0x6ED9EBA1
        elif 40 <= i <= 59:
            f = (b & c) | (b & d) | (c & d) 
            k = 0x8F1BBCDC
        elif 60 <= i <= 79:
            f = b ^ c ^ d
            k = 0xCA62C1D6

        a, b, c, d, e = ((left_rotate(a, 5) + f + e + k + w[i]) & 0xffffffff, 
                        a, left_rotate(b, 30), c, d)

    # Add this chunk's hash to result so far:
    h0 = (h0 + a) & 0xffffffff
    h1 = (h1 + b) & 0xffffffff 
    h2 = (h2 + c) & 0xffffffff
    h3 = (h3 + d) & 0xffffffff
    h4 = (h4 + e) & 0xffffffff

    return h0, h1, h2, h3, h4

def sha1(message):
    """SHA-1 Hashing Function
    A custom SHA-1 hashing function implemented entirely in Python.
    Arguments:
        message: The input message string to hash.
    Returns:
        A hex SHA-1 digest of the input message.
    """
    # Initialize variables:
    h0, h1, h2, h3, h4 = ini_variables()
    
    # Convert mesage to suitable format for hashing
    message = format_message(message)

    # Process the message in successive 512-bit chunks:
    # break message into 512-bit chunks
    for i in range(0, len(message), 64):
        w = [0] * 80
        # break chunk into sixteen 32-bit words w[i]
        for j in range(16):
            w[j] = struct.unpack(b'>I', message[i + j*4:i + j*4 + 4])[0]
        # Extend the sixteen 32-bit words into eighty 32-bit words:
        for j in range(16, 80):
            w[j] = left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)
    
        h0, h1, h2, h3, h4 = process_chunk(h0, h1, h2, h3, h4, w)
    
    # Produce the final hash value:
    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)
    
if __name__ == '__main__':
    print("Enter message to be encoded : ")
    msg = input()

    cipher = sha1(msg.encode())
    print(cipher)    