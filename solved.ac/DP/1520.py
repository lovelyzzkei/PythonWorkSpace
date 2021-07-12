import sys; read = sys.stdin.readline
sys.setrecursionlimit(10**9)
m, n = map(int, read().split())
MAP = list(list(map(int, read().split())) for i in range(m))
dp = [[-1 for _ in range(n)] for __ in range(m)]
dp[m-1][n-1] = 1    # 마지막 끝에 도착했을 경우를 대비

def dfs(y, x):
    if dp[y][x] == -1:  # 아직 방문하지 않은 경우
        dp[y][x] = 0    # 일단 방문 처리
        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ny=y+dy; nx=x+dx
            if 0<=ny<m and 0<=nx<n and MAP[ny][nx] < MAP[y][x]:
                dp[y][x] += dfs(ny, nx)
    return dp[y][x]

print(dfs(0, 0))