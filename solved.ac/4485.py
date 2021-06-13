import sys; read = sys.stdin.readline
import heapq

def dijkstra(y, x):
    q = []
    d = [[INF] * n for i in range(n)]
    d[y][x] = cave[y][x]
    heapq.heappush(q, (d[y][x], y, x))

    while q:
        cur_rupee, cur_y, cur_x = heapq.heappop(q)
        if d[cur_y][cur_x] < cur_rupee:
            continue
        
        for i in range(4):
            ny = cur_y + dy[i]; nx = cur_x + dx[i]
            if 0<=ny<n and 0<=nx<n:
                cost = cur_rupee + cave[ny][nx]
                if cost < d[ny][nx]:
                    d[ny][nx] = cost
                    heapq.heappush(q, (cost, ny, nx))

    return d[n-1][n-1]


n = int(read())

INF = int(1e5)
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
ret = []

while n:
    cave = [list(map(int, read().split())) for i in range(n)]
    ret.append(dijkstra(0, 0))
    n = int(read())

for idx, value in enumerate(ret):
    print(f'Problem {idx+1}: {value}')