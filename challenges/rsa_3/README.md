
# Algorithm Explanation

Atrisius is furious that you were able to intercept and decode his message. At least he is happy that he had not send Ophelia his Blockchain Account Passphrase that he had been planning to send in the previous message for her to purchase gifts. He soon figured out how you were able to decode his message and hence he changed the string encoding scheme such that you can't use your earlier methods to decrypt it. Now being assured that you will not be able to decrypt his message, he sends the encrypted passphrase to Ophelia.

To encode the message instead of breaking the string character wise, he broke the passphrase word by word and encoded each word by converting that word string into byte format and then converting it to integer equivalent (octet string to integer primitive). Then encrypting this set of encoded numbers using RSA, he sent the array of cipher numbers in the channel. You having lost a bet from the captain and unable to pay your dues, decide on to intercept and decrypt this passphrase so that you dont have to taste the salt of the ocean. You had a talk with Atrisius and you have figured out somehow that his passphrase is a common proverb.

Public Key is visible to everyone which are as follows:
n : 9854835922166297063
e : 8759869084763750353

# Problem Statement

Encrypted message = [3763957574838451255, 5269362823303103924, 7346831257341524785, 6695434056073209953, 9840400271506372414, 4273039314460387507, 6817283625742861191, 7346831257341524785, 8928902732293947839, 6779337446447117371]

Find out the original message sent.

# Access
You can look at the code and you have access to encryption server (with the same key value as in the problem).

# Solution
You do a Chosen Plaintext attack. Having the knowledge that it is a common proverb from the English Language, you try to match the encrypted numbers of different common words to the set of numbers in the cipher.

Answer : a bird in hand is worth two in the bush