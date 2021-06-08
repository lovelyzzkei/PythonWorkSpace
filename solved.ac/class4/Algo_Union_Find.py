MAX_SIZE = 10

# Union-Find의 기본적인 구현 방법
parent = {i:i for i in range(0, MAX_SIZE)}  # 각 노드의 부모 노드 저장

def find(x):
    # 루트 노드는 부모 노드 번호로 자기 자신을 가짐
    if parent[x] == x:
        return x

    else:
        # 다른 노드들은 각 노드의 부모 노드를 찾아 올라감
        return find(parent[x])

def union(x, y):
    x = find(x)
    y = find(y)

    # 각 트리의 루트 노드를 같게 만듬
    parent[y] = x


# 최악의 경우 가장 밑에서 제일 위까지 올라가야 하는 상황 발생 -> O(N)
# 이를 최적화 하는 방법으로 경로 압축 (Path compression)

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])     # 재귀를 이용하여 한번에 부모 노드를 root 노드로 바꿈
    return parent[x]

# union 연산 최적화
# rank에 트리의 높이를 저장하여 항상 높이가 더 낮은 트리를 높은 트리 밑에 넣는다
rank = {i:0 for i in range(0, MAX_SIZE)}

def union(x, y):
    # 두 노드의 루트 노드 
    x = find(x)     
    y = find(y)

    # 만약에 두 루트 노드가 같다면 이미 같은 트리에 있으므로 그냥 반환
    if x == y:
        return

    # union-by-rank 최적화
    # 항상 높이가 더 낮은 트리를 높이가 높은 트리 밑에 넣음.
    # 즉, 높이가 더 높은 쪽을 root로 삼음

    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x

        # 합친 후에 높이가 같다면 x의 높이  + 1
        if rank[x] == rank[y]:
            rank[x] += 1