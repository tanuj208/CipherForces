import hashlib
import os
from math import sqrt, ceil
from helper import *

def sha1(m):
    '''SHA-1 hash function'''
    hasher = hashlib.sha1()
    hasher.update(m)
    return hasher.digest()

def mgf1(seed, mlen):
    '''MGF1 mask generation function with SHA-1'''
    t = b''
    hlen = len(sha1(b''))
    for c in range(0, ceil(mlen / hlen)):
        _c = i2osp(c, 4)
        t += sha1(seed + _c)
    return t[:mlen]


def xor(data, mask):
    '''Byte-by-byte XOR of two byte arrays'''
    masked = b''
    ldata = len(data)
    lmask = len(mask)
    for i in range(max(ldata, lmask)):
        if i < ldata and i < lmask:
            masked += (data[i] ^ mask[i]).to_bytes(1, byteorder='big')
        elif i < ldata:
            masked += data[i].to_bytes(1, byteorder='big')
        else:
            break
    return masked

def oaep_encode(m, emLen = 1024, label = b''):
    '''EME-OAEP encoding'''
    mlen = len(m)
    lhash = sha1(label)
    hlen = len(lhash)
    ps = b'\x00' * (emLen - mlen - 2*hlen - 2)
    db = lhash + ps + b'\x01' + m
    seed = os.urandom(hlen)
    db_mask = mgf1(seed, emLen - hlen - 1)
    masked_db = xor(db, db_mask)

    seed_mask = mgf1(masked_db, hlen)
    masked_seed = xor(seed, seed_mask)
    
    return b'\x00' + masked_seed + masked_db

def oaep_decode(c, emLen = 1024, label = b''):
    '''EME-OAEP decoding'''
    lhash = sha1(label)
    hlen = len(lhash)
    _, masked_seed, masked_db = c[:1], c[1:1 + hlen], c[1 + hlen:]

    seed_mask = mgf1(masked_db, hlen)
    seed = xor(masked_seed, seed_mask)
    db_mask = mgf1(seed, emLen - hlen - 1)
    db = xor(masked_db, db_mask)
    _lhash = db[:hlen]
    assert lhash == _lhash
    i = hlen
    while i < len(db):
        if db[i] == 0:
            i += 1
            continue
        elif db[i] == 1:
            i += 1
            break
        else:
            raise Exception()
    m = db[i:]
    return m