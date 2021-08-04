import sys; read = sys.stdin.readline

n, k = map(int, read().split())
items = [[0, 0]]
for _ in range(n):
    items.append(list(map(int,read().split())))
bags = [0]
for _ in range(k):
    bags.append(int(read()))
dp = [[0 for i in range(k+1)] for j in range(2)]
items.sort()
bags.sort()
print(items)
print(bags)

for i in range(1, n+1):
    for j in range(1, k+1):
        m, v = items[i]
        if m <= bags[j]:
            dp[1][j] = max(dp[0][j-1] + v, dp[0][j])
        else:
            dp[1][j] = dp[0][j]
    # for item in dp:
    #     print(item)    
    if i == n:
        break
    dp[0] = dp[1][:]
    dp[1] = [0 for i in range(k+1)]

print(dp[1][k])