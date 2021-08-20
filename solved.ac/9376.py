import sys; read = sys.stdin.readline
import heapq
INF = int(1e5)

t = int(read())
ret = []
for tc in range(t):
    h, w = map(int, read().split())
    prison = []; prisoner = []
    for i in range(h):
        tmp = []; input = read().strip()
        for j in range(w):
            if input[j] == '*':
                tmp.append(-1)
            elif input[j] == '#':
                tmp.append(1)
            else:
                tmp.append(0)
                if input[j] == '$':
                    prisoner.append([i, j])
        prison.append(tmp)

    def inMap(y, x):
        return 0<=y<h and 0<=x<w

    def dijkstra(y, x):
        q = [[0, y, x, []]]
        d[y][x] = 0; ans = INF
        doorToOpen = []
        heapq.heapify(q)
        while q:
            dist, cy, cx, doors = heapq.heappop(q)
            if d[cy][cx] < dist:
                continue
            if cy==0 or cy==h-1 or cx==0 or cx==w-1:
                if dist < ans:
                    ans = dist
                    doorToOpen = doors
                    continue
            for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
                ny=cy+dy; nx=cx+dx
                if inMap(ny, nx) and prison[ny][nx] != -1:
                    cost = dist + prison[ny][nx]
                    if cost < d[ny][nx]:
                        d[ny][nx] = cost
                        if prison[ny][nx] == 1:
                            doors.append([ny, nx])
                            print(doors)
                            heapq.heappush(q, (cost, ny, nx, doors[:]))
                            doors.pop()
                        else:
                            heapq.heappush(q, (cost, ny, nx, doors[:]))
        print(doorToOpen)
        for i, j in doorToOpen:
            prison[i][j] = 0
        for item in d:
            print(item)
        return ans

    ans = 0
    for y, x in prisoner:
        d = [[INF for j in range(w)] for i in range(h)]
        ans += dijkstra(y, x)

    ret.append(ans)

print('\n'.join(str(x) for x in ret))