import sys

M = 1234567891
L = int(sys.stdin.readline())
apc = sys.stdin.readline().strip()

sum = 0
for i in range(L):
    hash = ord(apc[i]) - 96
    print(hash)
    sum += ((hash * pow(31, i)) % M)

print(sum % M)