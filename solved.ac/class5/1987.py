import sys; read = sys.stdin.readline

r, c = map(int, read().split())
MAP = []
visited = {chr(alpha):False for alpha in range(65, 91)}

for row in range(r):
    tmp = []
    col = read().strip()
    for t in range(c):
        tmp.append(col[t])
    MAP.append(tmp)

def inMap(y, x):
    return 0<=y<r and 0<=x<c

def dfs(y, x):
    ret = 1
    for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
        ny=y+dy; nx=x+dx
        if inMap(ny, nx) and not visited[MAP[ny][nx]]:
            visited[MAP[ny][nx]] = True
            ret = max(ret, dfs(ny, nx)+1)
            if ret == 26:
                return 26
            visited[MAP[ny][nx]] = False

    return ret

visited[MAP[0][0]] = True
print(dfs(0, 0))