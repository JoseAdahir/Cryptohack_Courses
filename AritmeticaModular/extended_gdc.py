def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
 
 
if __name__ == '__main__':
    a = int(input("a: "))
    b = int(input("b: "))
    gcd, x, y = extended_gcd(a, b)
    print('The GCD is', gcd)
    print(f'x = {x}, y = {y}')

