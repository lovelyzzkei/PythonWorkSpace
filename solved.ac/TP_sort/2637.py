import sys; read = sys.stdin.readline
from collections import deque
n = int(read())
m = int(read())
tree = {i:[] for i in range(1, n+1)}
inDegree = {i:0 for i in range(1, n+1)}

for _ in range(m):
    x, y, k = map(int, read().split())
    tree[y].append([x, k])  # x를 만드는데 y가 k개 필요
    inDegree[x] += 1

# print(inDegree)
# print(tree)    
def tp_sort():
    # inDegree가 0인 것들이 기본 부품
    q = deque([])
    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)

    # 각 제품이 몇 개의 기본 부품으로 구성되어 있는지 저장하는 딕셔너리
    total = {i:{j:0 for j in range(1, n+1)} for i in range(1, n+1)}
    for base in q:
        total[base] = "BASE"
    # print(total)

    while q:
        base = q.popleft()
        for mid, cnt in tree[base]:
            inDegree[mid] -= 1
            if total[base] != "BASE":   # 현재 다루고 있는 것이 중간 부품이라면
                for part, num in total[base].items():
                    total[mid][part] += num * cnt
            else:
                total[mid][base] += cnt
            if inDegree[mid] == 0:
                q.append(mid)
    
    ret = []
    for i, v in total[n].items():
        if total[i] == "BASE":
            ret.append(f"{i} {v}")
    return ret
print('\n'.join(x for x in tp_sort()))

