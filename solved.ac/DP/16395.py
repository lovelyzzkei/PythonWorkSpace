import sys; read = sys.stdin.readline
t = [[0 for _ in range(31)] for _ in range(31)]
t[1][1] = 1
for i in range(2, 31):
    for j in range(1, i+1):
        t[i][j] = t[i-1][j-1] + t[i-1][j]

n, k = map(int, read().split())
print(t[n][k])