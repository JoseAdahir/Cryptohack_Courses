import pwn 

string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

string = bytes.fromhex(string)
key = bytes([a ^ b for a,b in zip(string, b"crypto{")])

print(key)

key= key+b'y'

temp =  (pwn.xor(string,key))
print(temp)
