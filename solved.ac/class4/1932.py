import sys; read = sys.stdin.readline

n = int(read())
t = []
d = [[0] * n for i in range(n)]

for i in range(n):
    t.append(list(map(int, read().split())) + [0] * (n-i-1))

d[0][0] = t[0][0]

for i in range(n-1):
    for j in range(i+1):
        # d[i][j] = max(d[i-1][j-1], d[i-1][j]) + t[i][j]
        d[i+1][j] = max(d[i+1][j], d[i][j] + t[i+1][j])
        d[i+1][j+1] = max(d[i+1][j+1], d[i][j] + t[i+1][j+1])

print(max(d[n-1]))