import sys; read = sys.stdin.readline

n, k = map(int, read().split())

items = [0 for i in range(101)]
c = [0 for i in range(n)]

t = list(map(int, read().split()))
for i in t:
    items[i] += 1
print(items)
