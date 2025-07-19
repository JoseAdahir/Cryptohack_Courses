def gdcExt(a,b):
    r = a%b
    if b%r == 0:
        return r , 1, -(a//b)
    gdc, x, y = gdcExt(b,r)
    x -= y*(a//b)
    # print(f'{y = } {x = }')
    return gdc, y , x

a = int(input("Ingrese el numero a: "))
b = int(input("Ingrese el numero b: "))
if b>a:
    a,b = b,a
gdc,v,u = gdcExt(a,b)
print(f'{gdc =}')
print(f'inv {a}') 
print(f' {v =}')
print(f'inv {b}')
print(f' {u =}')
