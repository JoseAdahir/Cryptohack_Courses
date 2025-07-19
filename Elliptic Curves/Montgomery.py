#from scalarMultiplication import pointAddition
from Crypto.Util.number import inverse
#Suma en curvas elipticas de de Montgomery
def adition(P:(int, int), Q:(int,int), p:int, A: int, B:int)->(int,int):
    alfa: int = (Q[1]-P[1]) * inverse((Q[0]-P[0]),p) % p
    x3: int= (B*(alfa**2) - A -P[0] -Q[0]) % p
    y3: int = (alfa*(P[0]-x3) - P[1]) % p
    return (x3, y3)

#Suma del mismo elemento
def double(P:(int, int), p:int, A: int, B:int)->(int,int):
    alfa: int = (3*P[0]**2 + 2*A*P[0] + 1) * pow((2*B*P[1]),-1,p) % p
    x3: int = (B*(alfa**2) - A - 2*P[0]) %  p
    y3:int  = (alfa*(P[0]-x3) - P[1]) % p
    return (x3, y3)

#Montgomery's binary algorithm in group E(Fp)
def scalar_multiplication(P:(int, int),k:int, A:int, B:int, p:int)->(int,int):
    kn: list = list(map(int,bin(k)[2:])) 
    kn = kn[1:]
    R0:(int, int) = P
    R1:(int, int) = double(P,p,A, B)
    for j,i in enumerate(kn):
        if i == 0:
            R1 = adition(R0, R1, p,A, B)
            R0 = double(R0, p, A, B)
        else:
            R0 = adition(R0, R1,p,A, B)
            R1 = double(R1,p, A, B)
    return R0
            
A: int = 486662
B: int = 1
p: int = 2**255 - 19
gx: int  = 9
y2 = (pow(gx,3,p) + A*pow(gx,2,p)+ gx) %p

# Se obtuvo por medio de Tonelli-Shanks
y: int = 14781619447589544791020593568409986887264606134616475288964881837755586237401
print(pow(y,2,p))
if y2 == pow(y,2,p):
    print("Todo correcto")

k: int = int("0x1337c0decafe",16)

P: (int, int) = (gx, y)

result: (int, int) = scalar_multiplication(P,k,A,B,p)

print(result)



