from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests

mensaje_final = b''

def obtenerCifrado(plaintext):
    plaintext = plaintext.encode('utf-8').hex()

    Url = 'http://aes.cryptohack.org/ecb_oracle/encrypt/'+plaintext+'/'
    r = requests.get(Url)
    respuesta = r.json()
    ciphertext = respuesta['ciphertext']
    return ciphertext

base = b'\x10'*16
base = obtenerCifrado(base.decode('utf-8'))
base = base[:32]

plaintext = "YELLOW SUBMARINE"
cifrado = obtenerCifrado(plaintext)

while cifrado[-32::] != base:
    plaintext += 'Y'
    cifrado = obtenerCifrado(plaintext)
longitudFlag = (len(cifrado) - len(plaintext)*2 - 32)//2
print(longitudFlag)

for i in range(0,longitudFlag):
    plaintext += 'Y'
    cifrado = obtenerCifrado(plaintext)
    for c in range(33,127):
        mensajetem = pad(c.to_bytes(1,'big') + mensaje_final,16)
        tamComparacion = len(mensajetem)*2
        cifradoTemp = obtenerCifrado(mensajetem.decode('utf-8'))
        if cifradoTemp[:tamComparacion] == cifrado[(-1*tamComparacion)::]:
            mensaje_final = c.to_bytes(1,'big') + mensaje_final
            print(mensaje_final)
            break

print(f'{mensaje_final =}')


