import sys; read = sys.stdin.readline
from collections import deque

def can_eat(y, x, shark_size):
    return (0 < map_[y][x] < shark_size)

# 시간 줄이기
def bfs(y, x, time, shark_size, eat):
    dq = deque([[y, x]])    # BFS를 돌리기 위한 덱
    fishes = []
    visited = [[0 for j in range(N)] for i in range(N)]    # 시간도 같이 저장
    visited[y][x] = time    # 이전 단계까지의 시간 불러오기
    
    while dq:
        # 지금 덱에 거리가 가장 가까운 물고기가 있다고 하더라도
        # 그런 물고기가 더 있을 수 있으므로 해당 덱까지는 다 돌려봐야한다.
        qlen = len(dq)
        while qlen:
            cur = dq.popleft()  
            cury = cur[0]; curx = cur[1]   # 현재 상어의 위치 

            # 다음 좌표를 넣을 때 필요한 좌표만 넣기
            for i in range(4):
                ny = cury + dy[i]; nx = curx + dx[i]
                # 다음 이동할 좌표가 맵 내에 존재하고, 방문하지 않았을 경우
                if 0<=ny<N and 0<=nx<N and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[cury][curx] + 1
                    # 만약 다음 좌표가 이동이 가능한 좌표이면 이동
                    if map_[ny][nx] == 0 or map_[ny][nx] == shark_size:
                        dq.append([ny, nx])

                    # 만약 다음 좌표에 먹을 수 있는 물고기가 있다면 물고기 리스트에 삽입
                    elif 0< map_[ny][nx] < shark_size:
                        fishes.append([ny, nx])

            qlen -= 1

        # 덱의 크기만큼 돌리고 나서 리스트에 물고기가 있다는 것은 먹을 수 있는 물고기가 있다는 것
        # 그 중에서 가장 왼쪽 위의 물고기를 찾자.
        if fishes:
            ny, nx = min(fishes)
            map_[ny][nx] = 0
            min_time = visited[ny][nx]
            eat += 1
            if shark_size == eat:
                shark_size += 1; eat = 0
            return ny, nx, min_time, shark_size, eat

    # 고기가 아예 없는 경우
    print(time)
    exit(0)

N = int(read())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

map_ = []
visited = [[False for j in range(N)] for i in range(N)]

# 공간에 있는 정보 저장
for i in range(N):
    map_.append(list(map(int, read().strip().split())))

# 처음 상어의 위치 확인
for i in range(N):
    for j in range(N):
        if map_[i][j] == 9:
            y, x = i, j
            map_[i][j] = 0

# 고기를 다 먹을 때까지 반복
time, shark_size, eat = 0, 2, 0
while True:
    y, x, time, shark_size, eat = bfs(y, x, time, shark_size, eat)

