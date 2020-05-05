from hashlib import sha256

P = "20200429005847701826-ca6acb55fbee3ffc-" #"20200316203721206519-9a78dbcada43a6fd-"
T = "3ba7d"
# S = "01382781" #hex(int("0", base=16))
n = 0
S = hex(n).replace('0x', '')[::-1]
while sha256(f"{P}{S}".encode()).hexdigest().startswith(T) != True:
    n = n + 1
    S = hex(n).replace('0x', '')[::-1]
    print(S)