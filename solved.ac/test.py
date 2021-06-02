S = bin(pow(2, 20)  - 1)
print(S)
S = 0
S = int(bin(S | (1 << 2)), 2)
print(S)