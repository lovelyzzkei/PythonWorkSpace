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

    d = [[INF for j in range(w)] for i in range(h)]

    def inMap(y, x):
        return 0<=y<h and 0<=x<w

    # 죄수자 2명에 대해서 다익스트라 실행 -> 경로에 존재하는 문의 개수와 경로를 저장
    def dijkstra(y, x):
        q = [0, y, x, []]
        heapq.heapify(q)
        d[y][x] = 0
        ret = []
        
        while q:
            num_door, cy, cx, route = heapq.heappop(q)
            if d[cy][cx] < num_door:
                continue
            if 
