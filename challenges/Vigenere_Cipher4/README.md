
# Algorithm Explanation

Given a plaintext, a key is chosen and the key is made to cyclically repeat itself till the length of key is equal to length of plaintext.
Ex - If plaintext is heythere and key is cat, then the key would be cyclically repeated till it has length 8.
So final key would be catcatca

Each character of the plaintext and key is assumed to be in lowercase alphabets.

Now, each character from a - z is mapped to their alphabetical order from 0 - 25.

Let m[] be the mapping vector converting character to its alphabetical order. Ex - m[a] = 0, m[z] = 25

Ciphertext[i] = (m[Ciphertext[i - 1]] + m[Plaintext[i]] + m[key[i]]) % 26 for i > 0

The only change from vigenere cipher and this algorithm is that we are also considering the previous character of the ciphertext to get the current character of the ciphertext.

To get the character at position i of ciphertext, mapping of plaintext at position i and key at position i is added modulo 26.
The final number is converted back to the corresponding alphabetical character by reverse mapping.

Ex - Plaintext -> heythere  
     Key ->       catcatca  
     Ciphetext -> jervhxte  

# Problem Statement

Given an enrypted message, find the length of the key used to encrypt it.  
Encrypted Message = "xrzqpaqhcygsboxgtkgeyhttxqgozqjnkhrasdnvczxvtlhgehomfarova"

# Access
You can look at the code but you do not have access to encryption or decryption server.

# Solution
We cannot use the techniques of vigenere cipher here directly as there is no cyclic repetition but we can convert this encrypted message to another message which is the vigenere cipher of the plaintext.

Let Normal_Vigenere denote the vigenere ciphertext of the plaintext
and Modified_Vignere denote the ciphertext of the plaintext by this algorithm.

Modified_Vigenere[i] = (m[Modified_Vignere[i - 1]] + m[Plaintext[i]] + m[key[i]]) % 26  
Normal_Vigenere[i] = (m[Plaintext[i]] + m[key[i]]) % 26  
Modified_Vigenere[i] = (m[Modified_Vignere[i - 1]] + Normal_Vignere[i]) % 26  
Normal_Vigenere[i] = (Modified_Vignere[i] - Modified_Vignere[i - 1] + 26) % 26  

So we can get the Normal vignere cipher of a plaintext using the modified vigenere cipher using the operation defined on the above line.
Once we get the normal vigenere cipher of the plaintext, we can use the previously used techniques to find the plaintext by first finding the key and then using frequency analysis for the caeser cipher.

Plaintext = "tajmahalisoneofthesevenwondersoftheworlditislocatedinindia"
