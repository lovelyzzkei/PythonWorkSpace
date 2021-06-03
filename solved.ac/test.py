import sys; read = sys.stdin.readline
from collections import deque

def D(node):
    return [(node[0]*2)%10000, node[1]+'D']

def S(node):
    return [node[0]-1, node[1]+'S']

def L(node):
    # 한자리인 경우 의미 없음
    if node[0] % 10 == node[0]:
        return [node[0], node[1]+'L']
    first = node[0] // pow(10, len(str(node[0]))-1)
    last = node[0] % pow(10, len(str(node[0]))-1)
    new = last * 10 + first
    return [new, node[1]+'L']

def R(node):
    # 한자리인 경우 의미 없음
    if node[0] % 10 == node[0]:
        return [node[0], node[1]+'R']
    first = node[0] // 10
    last = node[0] % 10
    new = last * pow(10, len(str(node[0]))-1) + first
    return [new, node[1]+'R']




def bfs(a, b, ans):
    dq = deque([[a, ans]])

    while dq:
        node = dq.popleft()
        if node[0] == b:
            ret.append(node[1])
            return
        if node[0] not in visited:
            visited[node[0]] = True
            nextNode = [D(node), S(node), L(node), R(node)]
            for item in nextNode:
                if item[0] not in visited:
                    dq.append(item)
    

ret = []
visited = {}
for t in range(int(read())):
    ans = ''
    a, b = map(int, read().split())
    bfs(a, b, ans)

print('\n'.join(ret))