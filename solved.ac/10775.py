import sys; read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] == x:
        parent[x] = x - 1   # 본인 게이트 다 찼고 그 밑의 게이트들에 채울 수 있음
        return x
    parent[x] = find(parent[x])
    return parent[x]


G = int(read())
P = int(read())

parent = {i:i for i in range(G+1)}
isFull = False; ans = 0

for _ in range(P):
    gi = int(read())
    if isFull:
        continue

    now_gate = find(gi)
    if now_gate == 0:
        isFull = True
    else:
        ans += 1

print(ans)