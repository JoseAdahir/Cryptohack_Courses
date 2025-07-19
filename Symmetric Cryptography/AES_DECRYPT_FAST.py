from Crypto.Cipher import AES
import base64

KEY = input("Deme la llave").encode("utf-8")
if len(KEY) != 16:
    print("Esa llave no sirve, no es de 16 bytes")
    exit()
FLAG = input("Deme el texto")



def decrypt(ciphertext):
    ciphertext = base64.b64decode(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return 

    return decrypted


def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return encrypted.hex()

print(decrypt(FLAG))
