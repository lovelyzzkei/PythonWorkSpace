import sys; read = sys.stdin.readline
from collections import deque

# 시간 줄이기
def bfs(y, x, shark_size, eat):
    dq = deque([[y, x, 0]])    # BFS를 돌리기 위한 덱
    fishes = deque([])     # 먹을 수 있는 물고기들을 저장하기 위한 덱
    visited = [[False for j in range(N)] for i in range(N)]
    isSearched = False      # 가장 가까운 물고기가 발견되었는지를 확인하기 위한 플래그
    min_time = 9999         # 가장 가까운 물고기까지의 거리도 저장

    while dq:
        cur = dq.popleft()  
        cury = cur[0]; curx = cur[1]; cur_time = cur[2]    # 현재 상어의 위치
        visited[cury][curx] = True  

        # 가장 가까운 물고기가 발견되면 그 시점부터 큐에 있는 다른 원소들 제거
        if map_[cury][curx] > 0 and map_[cury][curx] < shark_size:
            fishes.append(cur)
            isSearched = True; min_time = min(min_time, cur_time)

        if isSearched:  # 가장 가까운 물고기가 발견되었다면 다른 공간 탐색할 필요가 없음
            continue

        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]

        for i in range(4):
            ny = cury + dy[i]; nx = curx + dx[i]
            # 다음 이동할 좌표가 맵 내에 존재하고, 방문하지 않았으며, 현재 상어의 크기보다 작거나 같은 물고기가 존재하는 경우
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx] and map_[ny][nx] <= shark_size:
                dq.append([ny, nx, cur_time+1])
        
    # while문이 끝났다는 것은 fish에 고기가 존재하거나 아예 없거나
    if len(fishes) == 0: return 0   # 고기가 아예 없는 경우

    # 고기가 있는 경우 가장 위에서 왼쪽의 고기를 찾아야 한다.
    minY = N; minX = N
    while fishes:
        fish = fishes.popleft()
        if fish[2] == min_time and fish[0] <= minY and fish[1] <= minX:
                minY = fish[0]; minX = fish[1]
#    print(f'({y}, {x}) -> ({minY}. {minX}), time: {min_time}')
    # 찾은 고기 먹고 다음 단계 진행
    map_[minY][minX] = 0
    eat += 1
    if shark_size == eat:   # 자기 자신의 크기만큼 먹었다면 크기 1 증가
        shark_size += 1; eat = 0
    return min_time + bfs(minY, minX, shark_size, eat)  # 고기를 먹은 위치부터 다시 진행


N = int(read())

map_ = []
visited = [[False for j in range(N)] for i in range(N)]

# 공간에 있는 정보 저장
for i in range(N):
    map_.append(list(map(int, read().strip().split())))

# 처음 상어의 위치 확인
for i in range(N):
    for j in range(N):
        if map_[i][j] == 9:
            map_[i][j] = 0
            print(bfs(i, j, 2, 0))