#!/usr/bin/python
salt = '7cb8d23734b9d4eb'.decode('hex')

import hashlib, binascii
from Crypto.Cipher import AES
import base64
from passlib.utils.pbkdf2 import pbkdf1

BLOCK_SIZE = 16

def pad(data):
    length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + (chr(length)*length).encode()

def hasher(algo, data):
    hashes = {'md5': hashlib.md5, 'sha256': hashlib.sha256,
    'sha512': hashlib.sha512}
    h = hashes[algo]()
    h.update(data)

    return h.digest()

# pwd and salt must be bytes objects
def openssl_kdf(algo, pwd, salt, key_size, iv_size):
    if algo == 'md5':
        temp = pbkdf1(pwd, salt, 1, 16, 'md5')
    else:
        temp = b''

    fd = temp    
    while len(fd) < key_size + iv_size:
        temp = hasher(algo, temp + pwd + salt)
        fd += temp

    key = fd[0:key_size]
    iv = fd[key_size:key_size+iv_size]

    print('salt=' + binascii.hexlify(salt).decode('ascii').upper())
    print('key=' + binascii.hexlify(key).decode('ascii').upper())
    print('iv=' + binascii.hexlify(iv).decode('ascii').upper())

    return key, iv

def encrypt(message):
    (key, iv) = openssl_kdf('md5', b'hello', salt, 32, 16)   
    aes = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(b"Salted__" + salt + aes.encrypt(pad(message)))

print(encrypt('test'))
