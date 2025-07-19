from PIL import Image
from io import BytesIO
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests

mensaje_final = b''

def obtenerCifrado():
    Url = 'https://aes.cryptohack.org/bean_counter/encrypt/'
    r = requests.get(Url)
    respuesta = r.json()
    encrypted = respuesta['encrypted']
    return encrypted

png_headers = bytes([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a, 0x00, 0x00, 0x00, 0x0d, 0x49, 0x48, 0x44, 0x52])
print(png_headers)

cifradoBytes = bytes.fromhex(obtenerCifrado())
cifradoBytes = [cifradoBytes[i:i+16] for i in range(0,len(cifradoBytes),16)]
nuevo = b''
const = bytes([a^b for a,b in zip(cifradoBytes[0],png_headers)])

for x in cifradoBytes:
    nuevo += bytes([a^b for a,b in zip(x,const)])
    

#print(nuevo)
with open('output.png','wb') as image_file:
    image_file.write(nuevo)

