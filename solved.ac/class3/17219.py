import sys; read = sys.stdin.readline

n, m = map(int, read().split())
password = {}
ret = []

for i in range(n):
    site, pw = read().strip().split()
    password[site] = pw

for i in range(m):
    ret.append(password[read().strip()])

print('\n'.join(ret))