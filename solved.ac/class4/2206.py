import sys; read = sys.stdin.readline
from collections import deque

def bfs(y, x, wall):
    dq = deque([[y, x, wall]])
    # 각 좌표마다 두 개의 방문처리 여부 
    # 하나는 벽을 뚫고 갔을 경우, 하나는 그렇지 않은 경우
    visited = [[[False, False] for j in range(m)] for i in range(n)]    
    dist = 1

    while dq:
        qlen = len(dq)
        while qlen:
            cury, curx, breakWall = dq.popleft()
            if cury == n-1 and curx == m-1:
                print(dist)
                return

            for i in range(4):
                ny = cury + dy[i]; nx = curx + dx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if breakWall:   # 벽을 이미 한번 뚫은 경우
                        if visited[ny][nx][0]:  # 벽을 뚫고 가면서 최단경로가 이미 존재한다면 패스
                            continue
                        if _map[ny][nx] == 1:   # 다음 좌표에 벽이 있으면 그냥 넘어감
                            continue
                        # 그렇지 않으면 벽을 뚫고 간 경우에 방문처리를 해주고 진행
                        visited[ny][nx][0] = True
                        dq.append([ny, nx, breakWall])
                    else:   # 벽을 아직 뚫지 않은 경우
                        if _map[ny][nx] == 1:   # 다음 좌표에 벽이 있다면
                            if not visited[ny][nx][0]:  # 그 벽으로 가는게 최단경로일 경우 방문처리
                                visited[ny][nx][0] = True
                                dq.append([ny, nx, True])
                        else:
                            if not visited[ny][nx][1]:
                                visited[ny][nx][1] = True
                                dq.append([ny, nx, breakWall])

            qlen -= 1
        dist += 1

    print(-1)
    return
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, read().split())

_map = []
for i in range(n):
    input = read().strip()
    temp = []
    for j in range(m):
        temp.append(int(input[j]))
    _map.append(temp)

bfs(0, 0, bool(_map[0][0]))