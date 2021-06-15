import sys; read = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(o, x, y):
    x = find(x); y = find(y)
    v1, v2 = rank[x], rank[y]
    if o == 1:
        parent[x] = y
        for i in range(1, n+1):
            if parent[i] == x:
                rank[x] += v2
        rank[y] += v1

    else:
        if rank[x] < rank[y]:
            rank[y] -= v1
            for i in range(1, n+1):
                if parent[i] == x:
                    rank[i] = 0
                if i != y and parent[i] == y:
                    rank[i] -= v1
        else:
            rank[x] -= v2
            for i in range(1, n+1):
                if parent[i] == y:
                    rank[i] = 0
                if i != x and parent[i] == x:
                    rank[i] -= v2


n, m = map(int, read().split())
parent = {i:i for i in range(1, n+1)}
rank = {i:0 for i in range(1, n+1)}

# 국가의 병력 저장
for i in range(1, n+1):
    rank[i] = int(read())

# 동맹, 전쟁 관계 =
# 동맹 -> rank 합침, 전쟁 -> rank 차이
for _ in range(m):
    o, p, q = map(int, read().split())
    union(o, p, q)

ret = []
for i in range(1, n+1):
    if rank[i] != 0:
        ret.append(rank[i])

ret = list(set(ret))
print(len(ret))
print(' '.join(str(x) for x in sorted(ret)))