import pwn

remote = True
if remote:
    io = pwn.remote('challenges2.france-cybersecurity-challenge.fr', 3001)
else:
    io = pwn.process(elf.path)

pwn.context.log_level = 'debug'

while True:
    try:
        r = io.recvuntil('What is a valid serial for username: ')
    except:
        break
    word = io.recvline().strip()
    answer = "".join([ chr(ord(c)^31) for c in word])[::-1]
    io.sendline(answer)
io.close()