import sys; read = sys.stdin.readline
n = int(read())
MAP = [list(map(int, read().split())) for _ in range(n)]
dp = [[[-1, 0] for _ in range(n)] for __ in range(n)]
# 가로:1, 세로:-1, 대각:0 으로 설정하여 각 방향마다 [dy, dx, 다음 방향]을 저장해놓음
mode = {1:[[0,1,1],[1,1,0]], -1:[[1,0,-1],[1,1,0]], 0:[[0,1,1],[1,0,-1],[1,1,0]]}  

# 이동하려는 좌표가 집 안에 있는지 + 벽이 있는지
def possible(cy, cx, dy, dx):
    if cy+dy<0 or cy+dy>=n or cx+dx<0 or cx+dx>=n:
        return False
    return not MAP[cy+dy][cx] and not MAP[cy][cx+dx] and not MAP[cy+dy][cx+dx]

dp[0][1][1] = 1
dp[n-1][n-1][0] = 1

def dfs(y, x, m):
    if dp[y][x][0] == -1:
        dp[y][x][0] = 0
        for dir in mode[m]:
            dy, dx, next_mode = dir
            if possible(y, x, dy, dx):
                ny=y+dy; nx=x+dx
                dp[y][x][1] = next_mode
                dp[y][x][0] += dfs(ny, nx, next_mode)

    for item in dp:
        print(item)
    print()
    
    if m != dp[y][x][1]:
        return 0
    else:
        return dp[y][x][0]

    
print(dfs(0, 1, 1))