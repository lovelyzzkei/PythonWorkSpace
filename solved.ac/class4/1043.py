import sys; read = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x); y = find(y)
    
    if x != y:
        parent[y] = x

n, m = map(int, read().split())
t = read().strip().split()
num_truth = int(t[0])
truth = []
if num_truth != 0:
    truth = [int(x) for x in t[1:]]

parent = {i:i for i in range(1, n+1)}
party = {i:0 for i in range(1, n+1)}    # 해당 파티의 parent 저장

for i in range(1, m+1):
    people = read().strip().split()
    num_people = int(people[0])
    people = [int(x) for x in people[1:]]

    for j in range(num_people):
        union(people[j-1], people[j])
        party[i] = people[j]

a = [find(x) for x in party.values()]
print(set(a) - set(truth))

