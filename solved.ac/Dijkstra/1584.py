import sys; read = sys.stdin.readline
import heapq

INF = int(1e5)
MAP = [[0 for _ in range(501)] for __ in range(501)]
dp = [[INF for _ in range(501)] for __ in range(501)]
dp[0][0] = 0

n = int(read())     # 위험한 구역의 수
for tc in range(n):
    x1, y1, x2, y2 = map(int, read().split())
    ax = max(x1, x2); bx = min(x1, x2)
    ay = max(y1, y2); by = min(y1, y2)
    for y in range(by, ay + 1):
        for x in range(bx, ax + 1):
            MAP[y][x] = 1

m = int(read())     # 죽음의 구역의 수
for tc in range(m):
    x1, y1, x2, y2 = map(int, read().split())
    ax = max(x1, x2); bx = min(x1, x2)
    ay = max(y1, y2); by = min(y1, y2)
    for y in range(by, ay + 1):
        for x in range(bx, ax + 1):
            MAP[y][x] = INF

def inMap(y, x):
    return 0<=y<501 and 0<=x<501

def dijkstra(y, x):
    q = []
    ans = INF
    heapq.heappush(q, (0, y, x))

    while q:
        hp, cy, cx = heapq.heappop(q)
        if (cy, cx) == (500, 500):
            ans = min(ans, hp)
            continue

        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ny = cy + dy; nx = cx + dx
            if inMap(ny, nx):
                if dp[ny][nx] < hp:
                    continue
                cost = hp + MAP[ny][nx]
                if MAP[ny][nx] != INF and cost < dp[ny][nx]:
                    dp[ny][nx] = cost
                    heapq.heappush(q, (cost, ny, nx))

    if ans == INF:
        return -1
    else:
        return ans

print(dijkstra(0, 0))