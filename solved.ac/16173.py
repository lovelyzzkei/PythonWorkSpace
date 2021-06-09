import sys; read = sys.stdin.readline
from collections import deque

def bfs(y, x):
    dq = deque([[y, x]])

    while dq:
        cur_y, cur_x = dq.popleft()

        if area[cur_y][cur_x] == -1:
            print("HaruHaru")
            return
        
        for i in range(2):
            # 젤리는 현재 영역에 쓰여있는 수 만큼 이동해야 함
            ny = cur_y + area[cur_y][cur_x] * dy[i]; nx = cur_x + area[cur_y][cur_x] * dx[i]    
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                visited[ny][nx] = True
                dq.append([ny, nx])
    
    # while문이 끝났다는 것은 끝점으로 갈 수 없다는 것
    print("Hing")
    return

n = int(read())
area = [list(map(int, read().split())) for i in range(n)]
visited = [[False for i in range(n)] for j in range(n)]
dy = [0, 1]
dx = [1, 0]

visited[0][0] = True
bfs(0, 0)