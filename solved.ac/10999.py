import sys; read = sys.stdin.readline

def init(start, end, node):
    if start == end:    # 리프 노드일 경우
        tree[node] = t[start]
        return tree[node]
    mid = (start+end)//2
    # 그렇지 않을 경우 현재 노드의 합은 양쪽 자식 노드의 합과 동일
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node]

def propagate(start, end, node):
    if lazy[node]:  # 현재 노드에 업데이트 해야 할 정보가 있다면 먼저 업데이트
        tree[node] += (end-start+1)*lazy[node]
        if start != end:    # 자식 노드가 존재한다면 밑으로 lazy값 전파
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        # 전파 이후 자기 자신의 lazy값은 0
        lazy[node] = 0

# 시작 idx, 끝 idx, 노드 번호, 업데이트 하는 범위, 업데이트 값
def update(start, end, node, idx_s, idx_e, diff): 
    # lazy 값이 존재하면 먼저 전파  
    propagate(start, end, node)

    # 현재 노드가 업데이트 하는 범위에서 벗어났다면 return
    if idx_e < start or idx_s > end:
        return

    if idx_s <= start and end <= idx_e:
        tree[node] += (end-start+1)*diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return

    mid = (start + end) // 2
    update(start, mid, node*2, idx_s, idx_e, diff)
    update(mid+1, end, node*2+1, idx_s, idx_e, diff)

    # 양쪽 업데이트 이후에 그 정보를 조상 노드에 한번 더 업데이트 시켜줌
    tree[node] = tree[node*2] + tree[node*2+1]


def sum(start, end, node, left, right):
    propagate(start, end, node)
    if right < start or left > end:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sum(start, mid, node*2, left, right) + sum(mid+1, end, node*2+1, left, right)

n, m, k = map(int, read().split())
tree = [0] * (4*n)
lazy = [0] * (4*n)
t = []

# 데이터가 존재하는 배열 받아오기
for _ in range(n):
    t.append(int(read()))

# 세그먼트 트리 생성
init(0, n-1, 1)
# update 또는 sum 수행
ret = []
for _ in range(m+k):
    input = list(map(int, read().split()))
    if input[0] == 1:   # 값 update
        b, c, d = input[1:]
        update(0, n-1, 1, b-1, c-1, d) 
    else:
        ret.append(sum(0, n-1, 1, input[1]-1, input[2]-1))
print('\n'.join(str(x) for x in ret))