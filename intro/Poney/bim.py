import pwn

# Convert sym.shell function address into little endian format
pwn.p64(0x00400676)