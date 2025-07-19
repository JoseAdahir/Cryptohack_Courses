from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from Crypto.Util.number import inverse
import math
# Función de suma de puntos bajo una curva eliptica modulo p
def pointAddition(P,Q,p,a):
    if P == 0:
        return Q
    if Q == 0:
        return P
    x1 = P[0]
    y1 = P[1]

    x2 = Q[0]
    y2 = Q[1]

    if x1==x2 and y1 == (-y2 % p):
        return 0
    if Q != P:
        lamb = (y2-y1) % p
        div = (x2 -x1) % p
        div = inverse(div,p)
        lamb = (lamb*div) % p
    else:
        lamb = (3*pow(x1,2,p) + a) % p
        div = 2*y1
        div = inverse(div,p)
        lamb = (lamb*div) % p
    x3 = (lamb**2 -x1 -x2)% p
    y3 = (lamb*(x1-x3) -y1) % p
    return (x3,y3)

def scalarMultiplication(P,n,p,a):
    Q = P
    R = 0
    while n>0:
        if n%2 == 1:
            R = pointAddition(R,Q,p,a)
        Q = pointAddition(Q,Q,p,a)
        n = math.floor(n/2)
    return R


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

p = 9739
n = 6534
a = 497
x = 4726
ysq = (x**3 + a*x + 1768)%p
print("Segun la respuesta:",ysq)
y = pow(ysq,((p+1)//4),p)

print("y =",y)
P = (x,y)


shared_secret = scalarMultiplication(P,n,p,a)[0]
print(shared_secret)
iv = 'cd9da9f1c60925922377ea952afc212c'
ciphertext = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'

print(decrypt_flag(shared_secret, iv, ciphertext))
