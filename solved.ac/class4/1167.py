import sys; read = sys.stdin.readline
from collections import deque

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x); y = find(y)

    if x!= y: parent[y] = x


def dfs(n):
    dq = deque([[n, 0]])
    
    while dq:
        cur, cur_h = dq.popleft()
        for next in tree[cur]:
            print(cur, next)
            if not visited[next[0]]:
                visited[next[0]] = True
                height.append(cur_h + next[1])
                dq.append([next[0], cur_h + next[1]])

    print(height)


v = int(read())
tree = {i:[] for i in range(1, v+1)}   # 트리를 저장할 딕셔너리
parent = {i:i for i in range(1, v+1)}   # 트리의 루트 노드를 찾기 위한 딕셔너리
visited = [False] * (v+1)
height = []     # 각 노드까지의 거리를 저장할 리스트

# 트리에 간선 정보 저장
for i in range(1, v+1):
    edge_info = list(map(int, read().split()))[1:-1]
    length = len(edge_info); idx = 0
    while length:      # 딕셔너리에 간선 정보 저장 [연결 노드, 거리]
        union(v, edge_info[idx])
        tree[i].append(edge_info[idx: idx+2])
        idx += 2; length -= 2

# 해당 트리의 루트 노드를 구하여 최대 길이 구함 -> but 루트 노드를 포함하지 않더라도 최대 길이가 나올 수 있음
# 백트래킹?
visited[parent[1]] = True
dfs(parent[1])

print(max(height))