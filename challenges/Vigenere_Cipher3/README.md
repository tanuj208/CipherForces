
# Algorithm Explanation

Given a plaintext, a key is chosen.
Final key is made by repeating the key once backwards and once in normal order again till the legth of the key is less than length of ciphertext.
Ex - If plaintext is heythere and key is cat, then the key would be cattacca, Here first cat is used, then tac, then cat and so on...

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
Encrypted Message = "lrmknjfghaoklrmjzwwglkklurizdvwglzkllrmtzqfghaoklrmknjwglzklurizdvwglukf"

# Access
You can look at the code but you do not have access to encryption or decryption server.

# Solution

On simple look, it does not seem like it technique similar to vigenere cipher can be used here, but observing carefully we can see that here we can consider a new key which is original_key + reverse_key. And this key is being used  as the key of the vigenere cipher.

Ex - if initial key is cat, then we can consider this to be a vigenere cipher with key "cattac" and solve in a similar manner. Here also after finding the key, we can make use of the fact that the key is a palindrome and get better results from frequency analysis in this case by taking into account positions of the key in a palindromic fashion like index 1 and index key_length, index 2 and index key_length - 1 and so on...

Plaintext = "thedogchasesthecatthecatchasestheratthemanchasesthedogtheratchasestheman"
