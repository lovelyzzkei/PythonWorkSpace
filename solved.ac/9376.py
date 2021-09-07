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

    def onEdge(y, x):
        return True if y==0 or y==h-1 or x==0 or x==w-1 else False

    def inMap(y, x):
        return 0<=y<h and 0<=x<w

    # 죄수자 2명에 대해서 다익스트라 실행 -> 경로에 존재하는 문의 개수와 경로를 저장
    def dijkstra(y, x):
        q = [[0, y, x, []]]
        heapq.heapify(q)
        d[y][x] = 0
        ret = []
        
        while q:
            num_door, cy, cx, route = heapq.heappop(q)
            if d[cy][cx] < num_door:
                continue
            if  onEdge(cy, cx):
                ret.append([num_door, route])
            
            for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
                ny=cy+dy; nx=cx+dx; tmp = route[:]
                if inMap(ny, nx) and prison[ny][nx] != -1:
                    cost = num_door + prison[ny][nx]
                    if cost < d[ny][nx]:
                        d[ny][nx] = cost
                        if prison[ny][nx] == 1:
                            tmp.append([ny, nx])
                        heapq.heappush(q, [cost, ny, nx, tmp])

        return ret
    
    prisoner1 = []; prisoner2 = []
    d = [[INF for j in range(w)] for i in range(h)]
    for t in dijkstra(prisoner[0][0], prisoner[0][1]):
        prisoner1.append(t)
    d = [[INF for j in range(w)] for i in range(h)]
    for t in dijkstra(prisoner[1][0], prisoner[1][1]):
        prisoner2.append(t)

    # print(prisoner1)
    # print(prisoner2)

    ans = INF
    for d1, r1 in prisoner1:
        for d2, r2 in prisoner2:
            tmp = r1.copy()
            tmp.extend(r2)
            ans = min(ans, len(list(set([tuple(item) for item in tmp]))))
    ret.append(ans)

print(' \n'.join(str(x) for x in ret))
