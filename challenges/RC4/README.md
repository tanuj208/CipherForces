# Algorithm Explanation

RC4 is a stream cipher and variable key length algorithm. The given implementation encrypts one character at a time. 
It uses a  pseudo-random generator to produce a character which is combined using XOR with the input stream. This pseudo-random generator generates random character by using key and the input stream.
You can read more about RC4 here: https://www.geeksforgeeks.org/rc4-encryption-algorithm/

# Problem Statement

Ciphertext: [46, 165, 10, 172, 227].
Find the plaintext which produces the given ciphertext on encryption. You can use our server to try out various plaintexts.

# Access
You have access to the encryption server.

# Solution
As it is a stream cipher. One character is encrypted at a time. So, a slightly optimized brute force approach works here. First character can be found by trying out all the possibilities. Similarly, Second character can then be found by trying all possible values for it by combining it with the correct first character and so on.
Plaintext: hello