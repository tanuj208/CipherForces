import json
import sys

class RC4:
    def __init__(self):
        """Initalize key and states"""
        
        self.p = 0
        self.q = 0
        self.state = [n for n in range(256)]
        self.key = self.get_key()

    def get_key(self):
        """Extract Keys from json file"""
        
        with open('keys.json') as f:
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

    def encrpyt(self, message):
        """Encrypt the given message"""
        self.set_state(self.key)
        cipher = [ord(c) ^ self.PRGA() for c in message]
        return cipher

def take_input():
    # plain_text = input("Enter the message to be encrypted: ")
    plain_text = sys.argv[1]
    return plain_text

if __name__ == '__main__':
    plain_text = take_input()
    rc4 = RC4()
    cipher = rc4.encrpyt(plain_text)
    print(cipher)