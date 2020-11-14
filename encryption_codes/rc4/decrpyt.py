import json

class RC4:
    def __init__(self):
        """Initalize key and states"""

        self.p = 0
        self.q = 0
        self.state = [n for n in range(256)]
        self.key = self.get_key()

    def get_key(self):
        """Extract Keys from json file"""
        
        with open('rc4/keys.json') as f:
            keys = json.load(f)
        return keys['key']

    def set_state(self, key):
        """Modify the states according to the key"""
        
        j = 0
        for i in range(256):
            j = (j + self.state[i] + key[i % len(key)]) % 256
            self.state[i], self.state[j] = self.state[j], self.state[i]

    def PRGA(self):
        """Pseudo Random Genration Algorithm"""
        
        self.p = (self.p + 1) % 256
        self.q = (self.q + self.state[self.p]) % 256
        self.state[self.p], self.state[self.q] = self.state[self.q], self.state[self.p]
        return self.state[(self.state[self.p] + self.state[self.q]) % 256]

    def decrpyt(self, message):
        """Decrypt the given message"""
        
        self.set_state(self.key)
        plain_data = [ord(c) ^ self.PRGA() for c in message]
        plain_text = ''.join(chr(c) for c in plain_data)
        return plain_text

def take_input():
    print("Enter message to be decrypted in the form of space separated integers: ")
    cipher_data = input().split()
    cipher_text = ''.join(chr(int(c)) for c in cipher_data)
    return cipher_text

if __name__ == '__main__':
    cipher_text = take_input()
    rc4 = RC4()
    plain_text = rc4.decrpyt(cipher_text)
    print(plain_text)