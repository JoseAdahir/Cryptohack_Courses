from Crypto.Cipher import AES
import hashlib
import random
import requests

ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
r = requests.get('https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words')
words = r.text.split('\n')
print(words)
# with open("/usr/share/dict/words") as f:
    # words = [w.strip() for w in f.readlines()]
    # print(words)
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = password_hash

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return str(e)

    return  decrypted

for i in words:
    KEY = hashlib.md5(i.encode()).digest()
    #Hacer request a la pagina de cryptPals y despues obtener el texto y comprobar que la versión desencriptada diga crypto
    plaintext = decrypt(ciphertext, KEY)
    if plaintext[0:6] == b'crypto':
        print(f"Llave {KEY} Mensaje = {plaintext}")
        break
print(KEY.decode("utf-8"))
