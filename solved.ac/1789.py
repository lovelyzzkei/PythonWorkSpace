import sys; read = sys.stdin.readline

s = int(read())

n = 0
while (n*(n+1))//3 > s or ((n+1)*(n+2))//2 <= s:
    n += 1

print(n)