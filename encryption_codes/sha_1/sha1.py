import struct
from helper import *

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