
def quadraticResidue(x, p):
    i=0
    x = x%p
    while i<p:
        j = i*i % p
        if j == x:
            print(f"{x} es residuo cuadratico de {i}")
            return i
        i+=1
    print(f"{x} no es residuo cuadratico")
quadraticResidue(14,29)
quadraticResidue(6,29)
quadraticResidue(11,29)
