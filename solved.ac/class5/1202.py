import sys; read = sys.stdin.readline
import heapq

n, k = map(int, read().split())
jewels = [list(map(int, read().split())) for _ in range(n)]
bags = []
for i in range(k):
    heapq.heappush(bags, int(read()))

jewels = sorted(jewels, key=lambda x:(x[0], -x[1]))

# print(jewels)
# # print(bags)

idx = 0
ans = 0
b = []

while len(bags) != 0:
    ci = heapq.heappop(bags)

    while idx < n and jewels[idx][0] <= ci:
        heapq.heappush(b, -jewels[idx][1])
        idx += 1
        # if idx == n:
        #     breaK

    if len(b) != 0:
        ans += (-heapq.heappop(b))

print(ans)