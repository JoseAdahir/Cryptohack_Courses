# import requests

# r = requests.get('http://socket.cryptohack.org:13371')

# data = {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0x4059b0e91480025ceaeba9310291d667e86d1162e41ddd1d3d5b58a1a6445f1ba8124bd96b2b7996871f0a301674f019092867742af3126676ed51cd33713b6a5f503dca3dd087c556e9fba3ca459f886723496dac44115ede3f2f88b0fe94d4b3259a2846570614038dfdeb0742515b0aa5178ad4b1999defec4ecf313923ef15cd3c031e10c232ac9cdbfe759776d8879fad371676c582fd1bbcca11f45498b0c03922ce8c3b24e8b7f9528a734c71d574f5a9974c60bd08c734d835ce4635"}

#!/usr/bin/env python3
import Crypto.Util.number as cu
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
PORT = 13371

r = remote(HOST, PORT)


def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

w = r.readline()
print(type(w))
print(w)
p = cu.bytes_to_long(bytes.fromhex("ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff"))
g = 2
b = 12345



B = hex(pow(g,b,p))
print(B)
print(type(B))

request = {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A":B }
json_send(request)


print(r.readline())

request = {"B":B }
json_send(request)

print(r.readline())

respuesta = {"iv": "ec97f14d5efdffdd79dd382bb6fedd62", "encrypted_flag": "d4fcc75c07eca2555559178d0768aec1b0c7928e78d0228efa3330e21e765042"}

iv = respuesta['iv']
encrypted = respuesta['encrypted_flag']


