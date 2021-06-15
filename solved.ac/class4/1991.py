import sys; read = sys.stdin.readline

def preorder(n):
    if n != '.':
        print(n, end='')
        if graph[n][0] != '.':
            preorder(graph[n][0])
        if graph[n][1] != '.':
            preorder(graph[n][1])
    
def inorder(n):
    if graph[n][0] != '.':
        inorder(graph[n][0])
    print(n, end='')
    if graph[n][1] != '.':
        inorder(graph[n][1])

def postorder(n):
    if graph[n][0] != '.':
        postorder(graph[n][0])
    if graph[n][1] != '.':
        postorder(graph[n][1])
    print(n, end='')

n = int(read())
graph = {chr(i+65) : ['',''] for i in range(n)}
for _ in range(n):
    node, left, right = read().split()
    graph[node][0] = left
    graph[node][1] = right

preorder('A')
print()
inorder('A')
print()
postorder('A')
