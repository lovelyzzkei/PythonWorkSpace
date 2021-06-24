import sys; read = sys.stdin.readline
card = {'A':1,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,\
    'J':11,'Q':12,'K':13}
n = int(read())
grid = [list(read().split()) for _ in range(n)]
dp = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(n):
    for j in range(n):
        grid[i][j] = card[grid[i][j][0]]

for i in range(n-1, -1, -1):
    for j in range(1, n+1):
        dp[i][j] = max(dp[i][j-1], dp[i+1][j]) + grid[i][j-1]

print(dp[0][n])