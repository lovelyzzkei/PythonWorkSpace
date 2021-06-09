import sys; read = sys.stdin.readline
from collections import deque

ans = []
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def bfs(y, x):
    global label

    ny, nx = h, w
    lowest_alti = regions[y][x]

    for i in range(4):
        y1 = y + dy[i]; x1 = x + dx[i]
        if 0 <= y1 < h and 0 <= x1 < w:
            if regions[y1][x1] < lowest_alti:
                lowest_alti = regions[y1][x1]
                ny = y1; nx = x1
                print(ny, nx)

    # 두 지형 합치는 과정
    if ny == h and nx == w: # 고립된 지형일 경우 새로운 지형
        basin[y][x] = label
        label = chr(ord(label) + 1)
        
    else:
        if basin[y][x] == '0':     # 현재 지형을 이미 있는 지형에 합치는 경우
            basin[y][x] = basin[ny][nx]

        if basin[ny][nx] == '0':    # 다음 지형을 현재 지형과 합치는 경우
            basin[ny][nx] = basin[y][x]

        if basin[y][x] == '0' and basin[ny][nx] == '0':    # 둘다 빈칸일 경우 새로운 지형
            basin[ny][nx] = label
            basin[y][x] = label
            label = chr(ord(label) + 1)

    print()
    print(ny, nx)
    for i in range(h):
        for j in range(w):
            print(basin[i][j], end=" ")
        print()


    


for t in range(int(read())):
    # 지형 정보 저장
    h, w = map(int, read().split())
    regions = [list(map(int, read().split())) for i in range(h)]
    basin = [['0' for j in range(w)] for i in range(h)]
    basin[0][0] = 'a'
    label = 'b'

    for i in range(h):
        for j in range(w):
            bfs(i, j)  

    ans.append(f'Case #{t+1}:')
    ans.append("\n".join([" ".join(basin[i]) for i in range(len(basin))]))
print("\n".join(x for x in ans))
