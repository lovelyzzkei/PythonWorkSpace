import sys; read = sys.stdin.readline

def mul(a, b, c):
    if b == 1:
        return a % c
    if b % 2 == 0:  # b가 짝수일 경우
        return (mul(a, b//2, c) ** 2) % c
    if b % 2 == 1:
        return (mul(a, b-1, c) * (a%c)) % c

a, b, c = map(int, read().split())
print(mul(a, b, c))