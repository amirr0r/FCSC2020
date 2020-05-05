import sys

file1_b = bytearray(open(sys.argv[1], 'rb').read())
x = file1_b[:16]
p = "1111111111111100"
i = 0
for c in x:
    j = 0
    #while chr(ord(c) ^ i) != p[j]:
    while chr(c ^ i) != p[j]:
            i = i + 1
    print(i)
    i = 0
    j = j + 1

