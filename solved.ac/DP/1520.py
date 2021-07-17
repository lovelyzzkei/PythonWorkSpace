import sys; read = sys.stdin.readline
m, n = map(int, read().split())
t = list(list(map(int, read().split())) for i in range(m))
# print(t)
dp = [[0 for _ in range(n)] for __ in range(m)]; dp[0][0] = 1
dy = [0, 1, 0]
dx = [1, 0, -1]

def inMap(y, x):
    return (0<=y<m and 0<=x<n)

def findPath():
    for y in range(m):
        for x in range(n):
            if dp[y][x] != 0:
                if y != 0 and dp[y-1][x] > dp[y][x]:  # 윗 줄의 최종 값 다시 갱신
                    dp[y][x] = dp[y-1][x]
                for k in range(3):
                    ny=y+dy[k]; nx=x+dx[k]
                    # print(inMap(ny, nx), t[ny][nx], t[y][x])
                    if inMap(ny, nx) and t[ny][nx] < t[y][x]:   # 지도 안에 있고 다음 칸이 현재 칸보다 낮을 경우에만 이동
                        dp[ny][nx] += dp[y][x]
    # for i in range(m):
    #     for j in range(n):
    #         print(dp[i][j], end=" ")
    #     print()
    return dp[m-1][n-1]
print(findPath())