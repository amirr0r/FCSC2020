import sys

query = sys.argv[1]

result=[]
i = 129
for c in query:
    while chr(255 ^ i) != c:
        i = i + 1
    result.append(hex(i).replace('0x', '%'))
    i = 129

print(f"(({'%ff' * len(sys.argv[1])})^({''.join(result)}))")