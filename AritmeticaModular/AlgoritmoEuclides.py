def algoritmoEuclides(a,b):
    if b < a:
        max = a
        min = b
    else:
        max = b
        min = a
    if (max%min) == 0 :
        return  min
    else:
        r = max%min
        return algoritmoEuclides(min,r)    


a = int(input("Ingrese el numero a: "))
b = int(input("Ingrese el numero b: "))
w = algoritmoEuclides(a,b)

print(w)
