import sys; read = sys.stdin.readline
from math import log2

def init(start, end, node):
    if start == end:
        tree[node] = t[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node]

def sum(start, end, node, left, right):
    if right < start or left > end:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sum(start, mid, node*2, left, right) + sum(mid+1, end, node*2+1, left, right)

def update(start, end, node, index, diff):  # start~end 에서 index 찾아 update
    if index < start or index > end:
        return 0
    tree[node] += diff
    if start == end:    # 리프 노드일 경우 업데이트 종료
        return 0
    mid = (start + end) // 2
    update(start, mid, node*2, index, diff)
    update(mid+1, end, node*2+1, index, diff)


n, m, k = map(int, read().split())
t = {0:0}
for i in range(1, n+1):
    t[i] = int(read())

tree = {i:0 for i in range(2**int(log2(n)+1)+1)}
init(1, n, 1)

ret = []
for i in range(m+k):
    a, b, c = map(int, read().split())
    if a == 1:
        diff = c - t[b]
        update(1, n, 1, b, diff)
        t[b] = c

    else:
        ret.append(sum(1, n, 1, b, c))

print('\n'.join(str(x) for x in ret))