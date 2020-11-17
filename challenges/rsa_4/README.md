
# Algorithm Explanation

Atrisius is exhausted now. He lost his girl, his money and his respect. What he has gained is experience and wisdom. With this wisdom he has finally able to create a foolproof method to encode any message. With all his experience now he uses a probabilistic OAEP padding along with the RSA encryption (https://tools.ietf.org/html/rfc8017#section-7.1). He has now declared over a million dollars to anyone who is able to find any shortcomings or weakness in this encryption scheme.

To encode the message he converts it to byte format which is then padded using the OAEP probabilistic padding. This padded message is then encrypted using RSA and sent. This is such a foolproof method that it has been mentions in PKCS (Public Key Cryptographic Standard).

Public Key is visible to everyone which are as follows:
n : 7848415872149439021741238378527046542155636918452173276578777832770834588164851214129702768648651451716503167230810105601276335074431232414560613192783289
e : 5894638853019078157932405124925351737661413066654850360754785572604028814660297190480492252917602895444544500533960637387341726125081957590134073598533903

# Problem Statement

Encrypted message = b'\x02\xa4\xae\x94$\xb4\x08\x08ENy\x18\xde\x88\xec\xd7\xae\\\x1b\xa6\x82\x17|\xb4\xfb\xd1\x1awO:\x16wD\x81`.^5\x1dz\xbc*\xdf\x82\x83\xdf\xa3\xe1\x8c\xa2s\xa7\xe1\xc5\x970\x0f\x1b\x13\xa0O\xa3;\x9d'

Find out the original message sent.

# Access
You can look at the code and you have access to encryption and decryption server (with the same key value as in the problem).

# Solution
Unsolved Problem

Answer : unbreakable