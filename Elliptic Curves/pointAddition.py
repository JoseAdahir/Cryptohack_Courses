from Crypto.Util.number import inverse

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
continuar = True
P = list(map(int,input("P: ").split()))
Q = list(map(int,input("Q: ").split()))
p = int(input("p: "))
a = int(input("a: "))
R = pointAddition(P,Q,p,a)
print("El resultado es",R)
respuesta = input("Quieres sumar otro punto?[s:si, n:no]")
if respuesta[0] == 'n':
    continuar = False
while(continuar):
    P = list(map(int,input("P: ").split()))
    R = pointAddition(P,R,p,a)
    print("El resultado es",R)
    respuesta = input("Quieres sumar otro punto?[s:si, n:no]")
    if respuesta[0] == 'n':
        continuar = False













