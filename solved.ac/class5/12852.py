import sys; read = sys.stdin.readline

n = int(read())
INF = int(1e7)
dp = {i:INF for i in range(1, n+1)}; dp[1] = 0
path = {i:[] for i in range(1, n+1)}

def pathCopy(i, j):
    tmp = []
    for item in path[j]:
        tmp.append(item)
    path[i] = tmp.copy()

for i in range(1, n+1):
    path[i].append(i)
    if i+1 <= n and dp[i] + 1 < dp[i+1]:
        dp[i+1] = dp[i] + 1
        path[i+1] = path[i].copy()

    if i*2 <= n and dp[i] + 1 < dp[i*2]:
        dp[i*2] = dp[i] + 1
        path[i*2] = path[i].copy()
    
    if i*3 <= n and dp[i] + 1 < dp[i*3]:
        dp[i*3] = dp[i] + 1
        path[i*3] = path[i].copy()

print(dp[n])
print(' '.join(str(x) for x in reversed(path[n])))