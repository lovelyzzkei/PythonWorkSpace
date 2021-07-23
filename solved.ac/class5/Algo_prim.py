import sys; read = sys.stdin.readline
import heapq

v, e = map(int, read().split())
graph = {i:[] for i in range(1, v+1)}
visited = [False] * (v+1)

for i in range(e):
    graph[a].append([c, b])     # [가중치, 도착점] 순으로 저장 (우선순위 큐 사용을 위하여)
    graph[b].append([c, a])

def prim(start):
    visited[start] = True   # 처음 노드 방문 처리
    candidate = graph[start]    # 처음 노드에서 갈 수 있는 노드들을 받아
    heapq.heapify(candidate)    # 우선순위 큐로 만듬 (간선의 가중치가 작은 것부터 처리하기 위하여)

    while candidate:
        w, v = heapq.heappop(candidate) # 가중치가 가장 작은 노드를 받음
        if not visited[v]:      # 방문을 안한 노드들 중에서
            visited[v] = True
            total_weight += w

            for e in graph[v]:  # 다음 노드에서 갈 수 있는 노드들 중에서
                if not visited[e[1]]:   # 아직 방문하지 않은 노드들만 뽑아 큐에 삽입(사이클 방지)
                    heapq.heappush(candidate, e)

    return total_weight

print(prim(1))