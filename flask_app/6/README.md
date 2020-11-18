
# Algorithm Explanation

Here comes the oldest and most widely used encryption algorithm, RSA. Now being a savvy in the ancient security algorithms, Acrisius decided to now implement his own version of the said algorithm. He read all about the algorithm in GFG (https://www.geeksforgeeks.org/rsa-algorithm-cryptography/) and decided to encode a String and give to you to see if you are able to decode it.

To encode the string he broke the string character wise and encoded the Unicode Number equivalent of the character to create an array of encoded numbers to denote the cipher. Your task is to find the string.
Public Key is visible to everyone which are as follows:
n : 221
e : 83

# Problem Statement

Encrypted message = [98, 136, 120, 43, 60, 74, 109, 64, 123, 143, 74]
Find out the original message used.

# Access
You can look at the code but you do not have access to encryption or decryption server (with the same key value as in the problem).

# Solution
Since the value of public key is so small one could use bruteforce to factorise n, Hence finally finding the private key according to the algorithm.

Answer : jf#1Skc&sAk