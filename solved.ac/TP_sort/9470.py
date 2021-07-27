import sys; read = sys.stdin.readline
from collections import deque

t = int(read())
ret = []
for tc in range(t):
    k, m, p = map(int, read().split())
    inDegree = {i:0 for i in range(1, m+1)}
    tree = {i:[] for i in range(1, m+1)}

    for _ in range(p):
        u, v = map(int, read().split())
        inDegree[v] += 1
        tree[u].append(v)
    # print(tree)
    # print(inDegree)

    def tp_sort():
        q = deque([])
        strahler = {i:[] for i in range(1, m+1)}
        for i in range(1, m+1): # 강의 근원인 노드들을 찾아 큐에 삽입
            if inDegree[i] == 0:
                q.append(i)
                strahler[i].append(1)
        
        # 해당 노드로 들어오는 강의 순서 중 가장 큰 값을 i라고 했을 때
        # 들어오는 모든 강 중에서 strahler 순서가 i인 강이 1개이면 순서는 i
        # 2개 이상이면 순서는 i+1
        while q:
            now = q.popleft()
            now_strahler = strahler[now]
            if now_strahler.count(max(now_strahler)) >= 2:
                now_strahler = strahler[now] = [max(now_strahler)+1].copy()
            else:
                now_strahler = strahler[now] = [max(now_strahler)].copy()

            for child in tree[now]:
                inDegree[child] -= 1
                strahler[child].append(now_strahler[0])
                if inDegree[child] == 0:
                    q.append(child)

            # print(strahler)

        return strahler[m][0]

    ret.append(tp_sort())

for i,v in enumerate(ret):
    print(f"{i+1} {v}")