import sys; read = sys.stdin.readline
from queue import Queue

def D(node):
    return [(node[0]*2)%10000, node[1]+'D']

def S(node):
    if node[0] == 0:
        return [9999, node[1]+'S']
    return [node[0]-1, node[1]+'S']

def L(node):
    first = node[0] // 1000
    last = node[0] % 1000
    new = last * 10 + first
    return [new, node[1]+'L']

def R(node):
    first = node[0] // 10
    last = node[0] % 10
    new = last * 1000 + first
    return [new, node[1]+'R']




def bfs(a, b, ans):
    dq = Queue()
    dq.put([a, ans])

    while dq:
        node = dq.get()
        if node[0] == b:
            ret.append(node[1])
            return
        if not visited[node[0]]:
            visited[node[0]] = True
            nextNode = [D(node), S(node), L(node), R(node)]
            for item in nextNode:
                if not visited[item[0]]:
                    dq.put(item)
    

ret = []

for t in range(int(read())):
    ans = ''
    visited = {i:False for i in range(0, 10000)}
    a, b = map(int, read().split())
    bfs(a, b, ans)

print('\n'.join(ret))