import sys; read = sys.stdin.readline

def preorder(n):
    if n != 0:
        print(n, end=' ')
        if graph[n][0] != 0:
            preorder(graph[n][0])
        if graph[n][1] != 0:
            preorder(graph[n][1])
    
def inorder(n):
    if graph[n][0] != 0:
        inorder(graph[n][0])
    print(n, end=' ')
    if graph[n][1] != 0:
        inorder(graph[n][1])

def postorder(n):
    if graph[n][0] != 0:
        postorder(graph[n][0])
    if graph[n][1] != 0:
        postorder(graph[n][1])
    print(n, end=' ')

n = int(read())
graph = {i : [0,0] for i in range(1, n+1)}
for _ in range(n):
    node, left, right = map(int, read().split())
    graph[node][0] = left
    graph[node][1] = right

preorder(1)
print()
inorder(1)
print()
postorder(1)
