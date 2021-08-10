import sys; read = sys.stdin.readline

n, k = map(int, read().split())
ai = list(map(int, read().split()))
citizens = {v:i+1 for i, v in enumerate(ai)}
sweets = {i:0 for i in range(1, n+1)}
# print(citizens)

id = sorted(ai)
common = k // n; k %= n

for i in range(k):
    sweets[citizens[id[i]]] += 1

print('\n'.join(str(x+common) for x in sweets.values()))
