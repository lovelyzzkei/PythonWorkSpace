import sys; read = sys.stdin.readline
from math import log2

def init(start, end, node):
    if start == end:
        tree[node][0] = t[start]
        return tree[node][0]
    mid = (start + end) // 2
    tree[node][0] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node][0]

def sum(start, end, node, left, right):
    if right < start or left > end:
        return 0
    if left <= start and end <= right:
        if tree[node][1]:   # lazy 존재
            print(tree[node])
            tree[node][0] += (end-start+1)*tree[node][1]
            if start != end:    # 자식 노드 존재
                tree[node*2][1] = tree[node*2+1][1] = tree[node][1]
            tree[node][1] = 0

        return tree[node][0]
    mid = (start + end) // 2
    return sum(start, mid, node*2, left, right) + sum(mid+1, end, node*2+1, left, right)

def update(start, end, node, idx_s, idx_e, diff):
    if idx_e < start or idx_s > end:
        return
    if idx_s <= start and end <= idx_e:
        tree[node][1] = diff
        return
    mid = (start + end) // 2
    update(start, mid, node*2, idx_s, idx_e, diff)
    update(mid+1, end, node*2+1, idx_s, idx_e, diff)


n, m, k = map(int, read().split())
t = {i:int(read()) for i in range(1, n+1)}; t[0] = [0]
tree = {i:[0, 0] for i in range(2**(int(log2(n))+1)+2)}
init(1, n, 1)

ret = []
for _ in range(m+k):
    temp = list(map(int, read().split()))
    if temp[0] == 1:
        b, c, d = temp[1:]
        update(1, n, 1, b, c, d)
        print(tree)
    else:
        ret.append(sum(1, n, 1, temp[1], temp[2]))

print('\n'.join(str(x) for x in ret))