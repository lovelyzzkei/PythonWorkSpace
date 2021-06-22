import sys; read = sys.stdin.readline

def init(y, start, end, node):
    if start == end:
        tree[y][node] = t[y][start]
        return tree[y][node]
    mid = (start + end) // 2
    tree[y][node] = init(y, start, mid, node*2) + init(y, mid+1, end, node*2+1)
    return tree[y][node]


def update(start, end, node, idx_y, idx_x, diff):
    if idx_x < start or idx_x > end:
        return
    tree[idx_y][node] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node*2, idx_y, idx_x, diff)
    update(mid+1, end, node*2+1, idx_y, idx_x, diff)

def sum(start, end, node, y, left, right):
    if right < start or left > end:
        return 0
    if left <= start and end <= right:
        return tree[y][node]
    mid = (start + end) // 2
    return sum(start, mid, node*2, y, left, right) + sum(mid+1, end, node*2+1, y, left, right)

n, m = map(int, read().split())
t = [list(map(int, read().split())) for j in range(n)]
tree = [[0] * (4*n) for i in range(n)]

for i in range(n):
    init(i, 0, n-1, 1)

ret = []
for _ in range(m):
    input = list(map(int, read().split()))
    if input[0] ==  0:
        y, x, val = input[1:]
        diff = val - t[y-1][x-1]
        update(0, n-1, 1, y-1, x-1, diff)
    else:
        ans = 0
        y1, x1, y2, x2 = input[1:]
        for y in range(y1-1, y2):
            ans += sum(0, n-1, 1, y, x1-1, x2-1)
        ret.append(ans)

print('\n'.join(str(x) for x in ret))