# Algorithm Description

Each character in plaintext is converted to its 8-bit ascii (in binary) & all binary numbers are concatenated.
The binary number is divided into 2 equal halves & following set of operations are applied two times:
	New left portion is equal to original right portion
	A random key is chosen
	New right portion is formed with xor of old left portion, old right portion & the random key.
	Old left portion = New left portion, Old right portion = New right portion
Left & right portions are concatenated to generate ciphertext.

# Problem Statement
You are given the ciphertext - ¢»ÖGåÊ & you are required to find the corresponding plaintext.
You are given another plaintext - ciphertext pairs generated using the same set of keys.
Plaintext = "helloo" (without quotes), Ciphertext = "¢¿ÚDáÄ" (without quotes)

# Access
You can look at the code but you do not have access to encryption or decryption server (with same set of keys as used in the problem).

# Solution
Using the plaintext-ciphertext pair (called the known plaintext attack), you can easily find the value of both keys. Then, using those keys, decryption is very easy.
How to find out the keys?
Let the left & right portion of plaintext is (L, R). If keys in rounds are k1 & k2 respectively. Then ciphertext generated will be (L xor R xor k1, L xor k1 xor k2) (Let it be (X, Y)). Now, k1 = X xor L xor R & k2 = Y xor L xor k1. 
Ans = kaboom
