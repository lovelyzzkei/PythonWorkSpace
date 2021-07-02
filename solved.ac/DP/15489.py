import sys; read = sys.stdin.readline
# 파스칼 삼각형
# (r, c)를 위 꼭짖점으로 하고, 한 변이 포함하는 수의 개수가 W인 정삼각형
# 정삼각형의 변과 내부에 존재하는 수들의 합을 구하자.
r, c, w = map(int, read().split())
dp = [[1 for i in range(r+w)] for j in range(r+w)]

for i in range(2, r+w):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

ans = 0
for i in range(r-1, r+w-1):
    for j in range(c-1, c-1+(i-r+2)):
        ans += dp[i][j]
print(ans)