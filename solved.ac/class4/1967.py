import sys; read = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(read())
tree = {i:[] for i in range(1, n+1)}
dp = [[] for _ in range(n+1)]
for t in range(n-1):
    u, v, w = map(int, read().split())
    tree[u].append([v, w])

# 간단하네
def treeDiameter(root):
    if tree[root] == []:     # 리프노드일 경우
        return 0
    for child, w in tree[root]:
        dp[root].append((w + treeDiameter(child)))
    return max(dp[root])

def sumNode(node):
    if len(node) == 0:
        return 0
    elif len(node) == 1:
        return node[0]
    else:
        tmp = node[:]
        tmp.sort()
        return (tmp[-1]+tmp[-2])

treeDiameter(1)
ans = 0
for node in dp:
    ans = max(ans, sumNode(node))

print(ans)