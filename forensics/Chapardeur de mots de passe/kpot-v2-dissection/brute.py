import sys

file1_b = bytearray(open(sys.argv[1], 'rb').read())
"""
# Try to guess the key 
x = file1_b[:16]
p = "1111111111111100"
i = 0
key = []
for c in x:
    j = 0
    #while chr(ord(c) ^ i) != p[j]:
    while chr(c ^ i) != p[j]:
            i = i + 1
    key.append(chr(i))
    i = 0
    j = j + 1
"""
key = ['t', 'D', 'l', 's', 'd', 'L', '5', 'd', 'v', '2', '5', 'c', '1', 'R', 'h', 'v']
#print("".join(key))
plain = []
x = file1_b[16:]
j = 0
for c in x:
	plain.append(chr(c ^ ord(key[j])))
	j = j + 1
	if j == len(key):
		j = 0
print("".join(plain))
