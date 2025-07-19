#!/usr/bin/env python3
from Crypto.Util.number import bytes_to_long
from pwn import * # pip install pwntools
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))

def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

HOST = "socket.cryptohack.org"
PORT = 13379

r = remote(HOST, PORT)

def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

print(r.readline())

resquest = {"supported": ["DH1536", "DH64"]}

json_send(resquest)

print(r.readline())
resquest = {"chosen": "DH64"}
json_send(resquest)
print(r.readline())



print(r.readline())
print(r.readline())

mensaje = {"iv": "28404452d840de02f1af1bafc8836621", "encrypted_flag": "94347c978be2bc0aaaab148cdd79a08c27f1f51f4297cfbd014af9e7082c668c"}

secret = 215263704416749034
iv = mensaje['iv']
encrypted = mensaje['encrypted_flag']

flag = decrypt_flag(secret,iv, encrypted)
print(flag)


