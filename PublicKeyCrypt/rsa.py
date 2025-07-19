import Crypto.Util.number 

def gdcExt(a,b):
    r = a%b
    if b%r == 0:
        return r , 1, -(a//b)
    gdc, x, y = gdcExt (b,r)
    x -= y*(a//b)
    # print(f'{y = } {x = }')
    return gdc, y , x

def calcD(e,p,q):
    N1 = (p-1)*(q-1)
    gdc, x, v = gdcExt(N1, e)

    return v

def rsaDec(c, d, n):
    mens = pow(c,d,n)
    longitud=(mens.bit_length()+7)//8
    plaintext = mens.to_bytes(longitud,'big')
    print(plaintext)
    return mens

def rsaDecExt(c, e, p, q):
    d = calcD(e,p,q)
    n = p*q
    mens = pow(c,d,n)
    longitud=(mens.bit_length()+7)//8
    plaintext = mens.to_bytes(longitud,'big')
    print(plaintext)
    return mens

prendido = True
while prendido:
    print("1 Obtener llave privada\n2 (Des)encriptar RSA con d\n3 Desencriptar RSA (c,e,p,q)\nq salir\n")
    x = input("Ingrese opción: ")
    if x == '1':
        e = int(input("Ingrese e: "))
        p = int(input("Ingrese p: "))
        q = int(input("Ingrese q: "))
        print(calcD(e,p,q))
    if x == '2':
        c = int(input("Ingrese c: "))
        d = int(input("Ingrese d: "))
        n = int(input("Ingrese n: "))
        print(rsaDec(c,d,n))
    if x == '3':
        c = int(input("Ingrese c: "))
        e = int(input("Ingrese e: "))
        p = int(input("Ingrese p: "))
        q = int(input("Ingrese q: "))
        print(rsaDecExt(c,e,p,q))
    input("\nPresione cualquier tecla para continuar\n\n")
    if x == 'q':
        prendido=False

