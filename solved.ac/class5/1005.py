import sys; read = sys.stdin.readline
from collections import deque

T = int(read())
ret = []
for t in range(T):
    n, k = map(int, read().split())
    time = {i+1:v for i, v in enumerate(list(map(int, read().split())))}
    in_degree = {i:0 for i in range(1, n+1)}
    building = {i:[] for i in range(1, n+1)}

    for _ in range(k):
        u, v = map(int, read().split())
        in_degree[v] += 1
        building[u].append(v)
    
    def topological_sort():
        q = deque([])
        cul_time = [[0] for _ in range(n+1)]
        # 진입 차수가 0인 정점들을 먼저 큐에 삽입
        for i in range(1, n+1):
            if in_degree[i] == 0:
                q.append(i)
        
        while q:
            now = q.popleft()
            time[now] += max(cul_time[now]) 
            for next_building in building[now]:
                in_degree[next_building] -= 1
                cul_time[next_building].append(time[now])
                if in_degree[next_building] == 0:
                    q.append(next_building)
            # print(cul_time)
            # print(time)

        return time[w]

    w = int(read())
    ret.append(topological_sort())

print('\n'.join(str(x) for x in ret))