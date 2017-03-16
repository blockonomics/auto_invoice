'''
Cryptographic functions to encrypt/decrypt data like CryptoJS
Adapted from
http://stackoverflow.com/questions/36762098/how-to-decrypt-password-from-javascript-cryptojs-aes-encryptpassword-passphras
'''
from Crypto import Random
from Crypto.Cipher import AES
import base64
import string
import random
from hashlib import md5

BLOCK_SIZE = 16

def pad(data):
    length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + (chr(length)*length).encode()

def unpad(data):
    return data[:-(data[-1] if type(data[-1]) == int else ord(data[-1]))]

def bytes_to_key(data, salt, output=48):
    # extended from https://gist.github.com/gsakkis/4546068
    assert len(salt) == 8, len(salt)
    data += salt
    key = md5(data).digest()
    final_key = key
    while len(final_key) < output:
        key = md5(key + data).digest()
        final_key += key
    return final_key[:output]

def encrypt(message, passphrase):
    salt = Random.new().read(8)
    key_iv = bytes_to_key(passphrase, salt, 32+16)
    key = key_iv[:32]
    iv = key_iv[32:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    aes = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(b"Salted__" + salt + aes.encrypt(pad(message)))

def decrypt(encrypted, passphrase):
    encrypted = base64.b64decode(encrypted)
    assert encrypted[0:8] == b"Salted__"
    salt = encrypted[8:16]
    key_iv = bytes_to_key(passphrase, salt, 32+16)
    key = key_iv[:32]
    iv = key_iv[32:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(encrypted[16:]))

def generate_passphrase(length):
  chars = string.letters + string.digits
  return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
  passphrase = generate_passphrase(8)
  pt = b'Hi Blockonomics!'
  ct = encrypt(pt, passphrase)
  decrypted_ct = decrypt(ct, passphrase)
  print("Plain text: " + pt)
  print("Cipher text: " + ct.encode('hex'))
  assert decrypted_ct == pt

  #print("pt", decrypt(encrypt(pt, password), password))
