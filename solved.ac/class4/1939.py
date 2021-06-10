import sys; read = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x); y = find(y)

    if x == y:
        return
    
    # 둘 중 하나가 진실을 알고 있으면 다른 한 사람도 진실을 알고 있는 것이 됨
    if know_true[x] or know_true[y]:
        know_true[x] = True; know_true[y] = True
        
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


n, m = map(int, read().split())

# 부모 노드, 트리의 높이, 진실을 알고 있는지의 여부를 저장하는 3개의 딕셔너리 선언
parent = {i:i for i in range(1, n+1)}
rank = {i:0 for i in range(1,n+1)}
know_true = {i: False for i in range(1, n+1)}
parties = []

# 진실을 알고 있는 사람은 플래그 True로 설정
truth = list(map(int, read().split()))
for person in truth[1:]:
    know_true[person] = True

for i in range(m):
    party = list(map(int, read().split()))
    for j in range(1, party[0]):
        union(party[j], party[j+1])

    parties.append(parent[party[1]])    # 대표 번호 저장

# 전체적으로 정리
for i in range(1, n+1):
    if know_true[find(i)]:
        know_true[i] = True

# 모두가 진실을 모른다면 파티 수만큼 출력
if truth[0] == 0:
    print(m)
else:
    ans = 0
    for party in parties:
        if not know_true[party]:
            ans += 1
    print(ans)
    