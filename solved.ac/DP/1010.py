import sys; read = sys.stdin.readline
f = [1] * 30
for i in range(2, 30):
    f[i] = i * f[i-1]
ret = []
for _ in range(int(read())):
    n, m = map(int, read().split())
    ret.append((f[m]//f[n])//f[m-n])
print('\n'.join(str(x) for x in ret))