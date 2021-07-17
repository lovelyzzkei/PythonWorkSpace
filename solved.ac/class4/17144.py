import sys; read = sys.stdin.readline
r, c, T = map(int, read().split())
tmp = [list(map(int, read().split())) for i in range(r)]
room = [[[0, 0] for i in range(c)] for j in range(r)]   # [미세먼지 양, 인접 방향에서 확산된 미세먼지의 양]
airCleaner = []

# 공기 청정기 좌표 구하기 & 새로 만든 room에 미세먼지 양 저장
for i in range(r):
    for j in range(c):
        if tmp[i][j] == -1:
            airCleaner.append([i, j])
        room[i][j][0] = tmp[i][j]

# print(room)
# T초 동안 미세먼지 확산 및 공기청정기 작동
for t in range(T):
    # 먼저 미세먼지 확산 (동시에 발생)
    for y in range(r):
        for x in range(c):
            if room[y][x][0] != -1:
                disperse_cnt = 0
                for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
                    ny=y+dy; nx=x+dx
                    if 0<=ny<r and 0<=nx<c and room[ny][nx][0] != -1:
                        disperse_amount = room[y][x][0] // 5
                        room[ny][nx][1] += disperse_amount
                        disperse_cnt += 1
                room[y][x][0] -= (disperse_amount * disperse_cnt)

    # 인접 방향에서 확산되어 들어온 양 더해주기
    for y in range(r):
        for x in range(c):
            room[y][x][0] += room[y][x][1]
            room[y][x][1] = 0

    # print()
    # for i in range(r):
    #     for j in range(c):
    #         print(room[i][j][0], end=" ")
    #     print()
    # print()

    # 공기 청정기 작동
    # 위로 순환하는 거 먼저 계산
    ac_y, ac_x = airCleaner[0]
    room[ac_y-1][0][0] = 0
    for y in range(ac_y-1, 0, -1):
        room[y][0][0] = room[y-1][0][0]
    for x in range(ac_x, c-1):
        room[0][x][0] = room[0][x+1][0]
    for y in range(0, ac_y):
        room[y][c-1][0] = room[y+1][c-1][0]
    for x in range(c-1, 1, -1):
        room[ac_y][x][0] = room[ac_y][x-1][0]
    room[ac_y][1][0] = 0

    # 그 다음 밑의 순환 구현
    ac_y, ac_x = airCleaner[1]
    room[ac_y+1][0][0] = 0
    for y in range(ac_y+1, r-1):
        room[y][0][0] = room[y+1][0][0]
    for x in range(0, c-1):
        room[r-1][x][0] = room[r-1][x+1][0]
    for y in range(r-1, ac_y, -1):
        room[y][c-1][0] = room[y-1][c-1][0]
    for x in range(c-1, 1, -1):
        room[ac_y][x][0] = room[ac_y][x-1][0]
    room[ac_y][1][0] = 0

# 미세먼지 양의 합 구하기
ans = 0
for i in range(r):
    for j in range(c):
        if room[i][j][0] != -1:
            ans += room[i][j][0]

print(ans)        
