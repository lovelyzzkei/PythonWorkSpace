import sys; read = sys.stdin.readline
import heapq
INF = int(1e6)

n, m = map(int, read().split())
y1, x1, y2, x2 = map(int, read().split())
MAP = [[0 for i in range(m)] for j in range(n)]
d = [[INF for i in range(m)] for j in range(n)]
d[y1-1][x1-1] = 0
MAP[y1-1][x1-1] == 0; MAP[y2-1][x2-1] = 1

for i in range(n):
    input = read().strip()
    for j in range(m):
        if (i, j) == (y1-1, x1-1) or (i, j) == (y2-1, x2-1):
            continue
        MAP[i][j] = int(input[j])

# print(MAP)
def inMap(y, x):
    return 0<=y<n and 0<=x<m

def dijkstra(y, x):
    q = []
    heapq.heappush(q, (0, y, x))

    while q:
        dist, cy, cx = heapq.heappop(q)
        if d[cy][cx] < dist:
            continue
        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ny = cy+dy; nx = cx + dx
            if inMap(ny, nx):
                cost = dist + MAP[ny][nx]
                if cost < d[ny][nx]:
                    d[ny][nx] = cost
                    heapq.heappush(q, (cost, ny, nx))

    # for item in d:
    #     print(item)
    return d[y2-1][x2-1]

print(dijkstra(y1-1, x1-1))