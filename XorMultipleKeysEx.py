llave1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
llave2_en = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
llave3_en = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_encrypted = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

llave1 = bytes.fromhex(llave1)
llave2_en = bytes.fromhex(llave2_en)
llave3_en = bytes.fromhex(llave3_en)
flag_encrypted = bytes.fromhex(flag_encrypted)

llave2 = bytes([a ^ b for a,b in zip(llave1,llave2_en)])

llave3 = bytes([a ^ b for a,b in zip(llave2, llave3_en)])

flag1 = bytes([a^b for a,b in zip(llave1,flag_encrypted)])

flag2 = bytes([a^b for a,b in zip(llave2, flag1)])

flag3 = bytes ([a^b for a,b in zip(llave3, flag2)])

flag_alt = bytes(a ^ b ^ c for a,b,c in zip(llave1, llave3_en,flag_encrypted))

print(flag3)

print(f"alt = {flag_alt}")

#Como vemos se puede reducir el encriptado en solo una linea (flag_alt) debido a que es asociativa
