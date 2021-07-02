import sys; read = sys.stdin.readline

r, c, t = map(int, read().split())
h = [list(map(int, read().split())) for i in range(r)]
tmp = [[0 for _ in range(c)] for __ in range(r)]
air_cond = []
for i in range(r):
    if h[i][0] == -1:
        air_cond.append([i, 0])
        air_cond.append([i+1, 0])
        break

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for _ in range(t):
    # 미세먼지 확산
    for i in range(r):
        for j in range(c):
            if h[i][j] > 0:
                disperse_amount = h[i][j] // 5
                disperse_cnt = 0
                for k in range(4):
                    ny=i+dy[k]; nx=j+dx[k]
                    if 0<=ny<r and 0<=nx<c:
                        tmp[ny][nx] += disperse_amount
                        disperse_cnt += 1
                h[i][j] -= (disperse_amount * disperse_cnt)

    # 공기청정기 작동
    