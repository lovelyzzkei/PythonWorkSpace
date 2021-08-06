import sys; read = sys.stdin.readline
LEN = 10

a = int('0b' + read(), 2)
print(bin(a))
b = int('0b' + read(), 2)
NOT = int(pow(2, LEN)-1)
print(bin(a & b)[2:].zfill(LEN))
print(bin(a | b)[2:].zfill(LEN))
print(bin(a ^ b)[2:].zfill(LEN))
print(bin(a ^ NOT)[2:].zfill(LEN))
print(bin(b ^ NOT)[2:].zfill(LEN))