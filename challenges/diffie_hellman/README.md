
# Algorithm Explanation

Given a generator g and a prime number p, Alice (sender) chooses a secret key a & Bob (receiver) chooses a secret key b. Public key of Alice is g^a % p, while secret key of Bob is g^b % p. Both Alice & Bob compute g^(ab) % p, & use it as their super key.

For encryption, each character of input text is converted to its 8-bit binary ascii number. Then, binary numbers of all characters are concatenated to make a bigger binary number, which is then converted to an 10-base integer.

This integer is then encrypted, by adding it to the super key & taking the modulus p. Then, this encrypted integer is converted in its binary form (numbers of bits are increased by a minimum amount such that it becomes divisble by 8). Every 8-bits are converted to a character and resulted string is the encrypted text.

Exactly reverse is done in decryption

# Problem Statement

g = 43
p = 1026641107730399495345298408059
Public key of Alice (sender) = 929293739471222707
Public key of Bob (receiver) = 361900299138566461283916594674
Encrypted message = \x04sÍÃkÑ\x00\x04\x89\x10å\x8a)
Find out the original message used.

# Access
You can look at the code but you do not have access to encryption or decryption server (with the same key value as in the problem).

# Solution
Since value of generator is very small & you can see that public key of Alice is way smaller than prime p, secret key of Alice is also small. You can do a bruteforce search on Alice's secret key & get it. Then, you can compute the super key & break the algorithm.
