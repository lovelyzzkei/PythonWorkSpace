import sys; read = sys.stdin.readline
# 밑작업
v = int(read())
tree = {i:[] for i in range(1, v+1)}
dp = [[] for _ in range(v+1)]
visited = {i:False for i in range(1, v+1)}

for tc in range(v):
    input = list(map(int, read().split()))[:-1]
    nodeNum = input[0]
    for k in range((len(input)-1)//2):
        u, d = input[2*k+1], input[2*k+2]
        tree[nodeNum].append([u, d])
# print(tree)

def treeDiameter(root):
    nodes = tree[root]
    if len(nodes) == 1 and visited[nodes[0][0]]:
        return 0
    visited[root] = True
    for child, w in nodes:
        if not visited[child]:
            dp[root].append(w+treeDiameter(child))
    return max(dp[root])

def sumNode(node):
    if len(node) == 0: return 0
    if len(node) == 1: return node[0]
    else:
        node.sort()
        return (node[-1]+node[-2])

treeDiameter(1)
ans = 0
for node in dp:
    ans = max(ans, sumNode(node))
print(ans)