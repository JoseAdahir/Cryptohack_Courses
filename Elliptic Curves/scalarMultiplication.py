from Crypto.Util.number import inverse
import math
import hashlib
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

#main
if __name__ == '__main__':
    continuar = True
    P = list(map(int,input("P: ").split()))
    n = int(input("n: "))
    p = int(input("p: "))
    a = int(input("a: "))
    R = scalarMultiplication(P,n,p,a)
    print("El resultado es",R)

    sha1 = hashlib.sha1()
    sha1.update(str(R[0]).encode("ascii"))
    key = sha1.digest()
    print("Hash:",key)
    print("Hash hex:",key.hex())




