import json
import random

def take_input():
    len_key = int(input("Length of the key in chars: "))
    return len_key

def store_key(len_key):
    key = []
    for i in range(len_key):
        key.append(random.randint(0,255))
    keys = {}
    keys['key'] = key
    with open('keys.json', 'w+') as f:
        json.dump(keys, f)

if __name__ == '__main__':
    len_key = take_input()
    store_key(len_key)