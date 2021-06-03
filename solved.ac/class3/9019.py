import sys; read = sys.stdin.readline
from collections import deque

def DSLR(node):
    d1 = node // 1000
    d2 = node // 100 - d1 * 10
    d3 = node // 10 - d1 * 100 - d2 * 10
    d4 = node % 10

    d = (node*2)%10000
    s = (node-1 if node != 0 else 9999)
    l = ((d2 * 10 + d3) * 10 + d4) * 10 + d1
    r = ((d4 * 10 + d1) * 10 + d2) * 10 + d3

    return [d, s, l, r]


def bfs(a, b):
    dq = deque([[DSLR(a), '']])
    while dq:
        nextNode = dq.popleft()
        for idx, way in enumerate(nextNode[0]):
            if idx == 0:
                last = 'D'
            if idx == 1:
                last = 'S'
            if idx == 2:
                last = 'L'
            if idx == 3:
                last = 'R'

            if way == b:
                ret.append(nextNode[1] + last)
                return
            elif not visited[way]:
                visited[way] = True
                dq.append([DSLR(way), nextNode[1] + last])
    

ret = []

for t in range(int(read())):
    visited = {i:False for i in range(0, 10000)}
    a, b = map(int, read().split())
    bfs(a, b)

print('\n'.join(ret))