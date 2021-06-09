import sys; read = sys.stdin.readline
from collections import deque

def bfs(x, y, wood):
    dq = deque([[x, y, wood]])

    while dq:
        qlen = len(dq)
        while qlen:
            cur_y, cur_x, cur_wood = dq.popleft()

            # 지금 바닥 장식 모양이 '-'이면 양 옆으로만 갈 수 있음
            if cur_wood == '-':
                for i in range(1, 4, 2):
                    ny = cur_y + dy[i]; nx = cur_x + dx[i]
                    if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                        if floor[ny][nx] == '-':
                            visited[ny][nx] = True
                            dq.append([ny, nx, '-'])
            
            # 지금 바닥 장식 모양이 '|'이면 위 아래로만 갈 수 있음
            if cur_wood == '|':
                for i in range(0, 3, 2):
                    ny = cur_y + dy[i]; nx = cur_x + dx[i]
                    if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                        if floor[ny][nx] == '|':
                            visited[ny][nx] = True
                            dq.append([ny, nx, '|'])

            qlen -= 1
    
    # while 문이 끝났다는 것은 더 이상 인접한 나무판자가 존재하지 않음
    return 1
            


n, m = map(int, read().split())

# '-' 모양과 '|' 모양 저장
floor = []
for i in range(n):
    input = read().strip()
    temp = []
    for j in range(m):
        temp.append(input[j])
    floor.append(temp)

visited = [[False for j in range(m)] for i in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
ans = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            ans += bfs(i, j, floor[i][j])

print(ans)