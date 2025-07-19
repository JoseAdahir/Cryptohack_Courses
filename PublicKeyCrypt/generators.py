import gmpy2

def esGenerador(g,p):
    w = {g}
    for j in range(2,p):
        w.add(pow(g,j,p))
        if len(w)!= j:
            return False
    return True
from primefac import primefac

p = 28151
i = 2


print(list(primefac(p-1)))

while i < 28151:
    if gmpy2.is_prime(i):
        print(f'Provando con {i}')
        if esGenerador(i,p):
            print(f'{i} es el generador más pequeño')
            exit()
    i+=1









