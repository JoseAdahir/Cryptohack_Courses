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
print(base)
plaintext = "YELLOW SUBMARINE"
cifrado = obtenerCifrado(plaintext)
tamañoBase = len(cifrado)
nuevoTamaño = tamañoBase
while tamañoBase == nuevoTamaño:
    plaintext += 'Y'
    cifrado = obtenerCifrado(plaintext)
    nuevoTamaño = len(cifrado)
    if cifrado[-32::] == base:
        plaintext += 'Y'
        cifrado = obtenerCifrado(plaintext)
        nuevoTamaño = len(cifrado)
        for c in range(33,127):
            mensajetem = mensaje_final + c.to_bytes(1,'big')
            cifradoTemp = obtenerCifrado(pad(mensajetem,16).decode('utf-8'))
            if cifradoTemp[:32] == cifrado[-32::]:
                mensaje_final = c.to_bytes(1,'big') + mensaje_final
                print(mensaje_final)
                break
for i in range(0,14):
    plaintext += 'Y'
    cifrado = obtenerCifrado(plaintext)
    nuevoTamaño = len(cifrado)
    for c in range(33,127):
        mensajetem = c.to_bytes(1,'big') + mensaje_final
        cifradoTemp = obtenerCifrado(pad(mensajetem,16).decode('utf-8'))
        if cifradoTemp[:32] == cifrado[-32::]:
            mensaje_final = c.to_bytes(1,'big') + mensaje_final
            print(mensaje_final)
            break

plaintext += 'Y'
cifrado = obtenerCifrado(plaintext)
nuevoTamaño = len(cifrado)
for c in range(33,127):
    mensajetem = c.to_bytes(1,'big') + mensaje_final
    cifradoTemp = obtenerCifrado(pad(mensajetem,16).decode('utf-8'))
    if cifradoTemp[:64] == cifrado[-64::]:
        mensaje_final = c.to_bytes(1,'big') + mensaje_final
        print(mensaje_final)
        break
for i in range(0,9):
    plaintext += 'Y'
    cifrado = obtenerCifrado(plaintext)
    nuevoTamaño = len(cifrado)
    for c in range(33,127):
        mensajetem = c.to_bytes(1,'big') + mensaje_final
        cifradoTemp = obtenerCifrado(pad(mensajetem,16).decode('utf-8'))
        if cifradoTemp[:64] == cifrado[-64::]:
            mensaje_final = c.to_bytes(1,'big') + mensaje_final
            print(mensaje_final)
            break
print(mensaje_final)

#idea para hacerlo más dinamico sabemos que seria un for 25 
#que tamCompa = len(pad(mensajetem, 16))*2
#y las variables fuese asi cifradoTemp [:tamCompa] == cifrado [-tamCompa ::]

