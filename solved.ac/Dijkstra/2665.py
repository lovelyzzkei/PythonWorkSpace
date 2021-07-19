import sys; read = sys.stdin.readline
import heapq

n = int(read())
maze = []
for t in range(n):
    tmp = []
    input = read().strip()
    for _ in range(n):  # 흰방을 0으로 검은 방을 1로 표시
        if int(input[_]) == 0:
            tmp.append(1)
        else:
            tmp.append(0)
    maze.append(tmp)

# print(maze)
def inMap(y, x):
    return 0<=y<n and 0<=x<n

def dijkstra(y, x):
    INF = int(1e4)
    ret = INF
    dp = [[INF for _ in range(n)] for __ in range(n)]
    dp[y][x] = 0

    q = []
    heapq.heappush(q, (0, y, x))

    while q:
        numBlack, cy, cx = heapq.heappop(q)

        if cy == n-1 and cx == n-1:
            ret = min(ret, numBlack)
            continue
        
        if dp[cy][cx] < numBlack:
            continue

        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ny=cy+dy; nx=cx+dx
            if inMap(ny, nx):
                cost = dp[cy][cx] + maze[ny][nx]
                if cost < dp[ny][nx]:
                    dp[ny][nx] = cost
                    heapq.heappush(q, (cost, ny, nx))
                
    # for item in dp:
    #     print(item)
    # print()
                
    return ret
                

print(dijkstra(0, 0))