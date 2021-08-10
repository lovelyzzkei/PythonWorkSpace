n = int(input())

def parity(n):
    print(n, n&1)
    return n & 1 + parity(n>>1) if n>=1 else 0
print(11&1)
print(parity(n))