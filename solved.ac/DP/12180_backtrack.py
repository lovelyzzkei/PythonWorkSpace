import sys; read = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(read())

ret = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x, dir):
    global count
    s = [[y, x, dir]]

    while s:
        cy, cx, cdir = s.pop()
        hasPath = False
        for i in range(2):
            ny = cy + dy[(cdir+i)%4]; nx = cx + dx[(cdir+i)%4]
            if 0<=ny<r and 0<=nx<c and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(ny, nx, dir+i)
                hasPath = True
                visited[ny][nx] = False

        if not hasPath:
            count += 1
            return



for _ in range(t):
    r, c = map(int, read().split())
    visited = [[False for i in range(c)] for j in range(r)]
    visited[r-1][0] = True
    count = 0
    dfs(r-1, 0, 0)
    ret.append(count)

for idx, ans in enumerate(ret):
    print(f"Case #{idx+1}: {ans}")