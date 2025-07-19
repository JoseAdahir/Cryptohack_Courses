string = "label"

def Xor(string, num):
    new_string = bytes(string,"utf-8")
    return bytes([a ^ num for a in new_string])

new_string = (Xor(string, 13)).decode("utf-8")

print(new_string)


