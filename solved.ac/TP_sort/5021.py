import sys; read = sys.stdin.readline
from collections import deque

n, m = map(int, read().split())
king = read().strip()
in_degree = {}; family = {}; blood = {}
in_degree[king] = 0

for _ in range(n):
    child, p1, p2 = read().strip().split()
    blood[child] = blood[p1] = blood[p2] = 0
    try:
        family[p1].append(child)
    except:
        family[p1] = [child]
    try:
        family[p2].append(child)
    except:
        family[p2] = [child]
    try:
        if in_degree[p1]:
            pass
    except:
        in_degree[p1] = 0
    try:
        if in_degree[p2]:
            pass
    except:
        in_degree[p2] = 0
    in_degree[child] = 2
print(in_degree)
def tp_sort():
    q = deque([king])
    blood[king] = 1

    while q:
        parent = q.popleft()
        for child in family[parent]:
            blood[child] += blood[parent] / 2
            in_degree[child] -= 1
            if in_degree[child] == 0:
                q.append(child)

        # 진입차수가 0인 노드들을 탐색하여 삽입
        for n, v in in_degree.items():
            if v == 0:
                q.append(n)

        print(blood)

tp_sort()
print(blood)
ans = 0
new_king = ''
for _ in range(m):
    name = read().strip()
    if blood[name] > ans:
        new_king = name[:]

print(new_king)