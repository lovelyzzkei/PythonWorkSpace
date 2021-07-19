import sys; read = sys.stdin.readline
from collections import deque

n = int(read())
in_degree = {i:0 for i in range(1, n+1)}
tree = {i:[] for i in range(1, n+1)}    # {parent:[child]} 로 저장
time = {i:0 for i in range(1, n+1)}     # 해당 작업을 완료하기 위한 최소 시간을 저장하는 인접 리스트

for node in range(1, n+1):
    tmp = list(map(int, read().split()))
    time[node] = tmp[0]     # 해당 작업이 걸리는 시간
    numParent = tmp[1]       # 해당 작업에 대해 선행 관계에 있는 작업들의 개수(부모의 개수)
    if numParent == 0:       # 선행 관계가 없는 작업들은 그냥 저장
        continue
    parents = tmp[2:]

    for parent in parents:
        tree[parent].append(node)
        in_degree[node] += 1

# print(in_degree)
# print(tree)
# print(time)

def tp_sort():
    # 진입차수가 0인 노드들을 먼저 삽입하여 위상정렬 준비
    q = deque([])
    for node in range(1, n+1):
        if in_degree[node] == 0:
            q.append(node)
    
    # 다양한 경로를 통해 해당 작업까지 완료하는데 걸리는 시간들을 저장해둔 인접 리스트
    cul_time = {i:[0] for i in range(1, n+1)}

    while q:
        now = q.popleft()
        time[now] += max(cul_time[now])
        for child in tree[now]:
            in_degree[child] -= 1
            cul_time[child].append(time[now])
            if in_degree[child] == 0:
                q.append(child)

    print(max(time.values()))

tp_sort()