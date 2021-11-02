import sys; read = sys.stdin.readline

n, k = map(int, read().split())
jewels = [list(map(int, read().split())) for _ in range(n)]
bags = [int(read()) for _ in range(k)]

jewels = sorted(jewels, key=lambda x:(-x[1], x[0]))
bags = sorted(bags)

# print(jewels)
# print(bags)

ans = []

for j in jewels:
    m, v = j
    for b in bags:
        if m <= b:
            bags.remove(b)
            ans.append(v)
            break

    bags.sort()

# print(ans)
print(sum(ans))

