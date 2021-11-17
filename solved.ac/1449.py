import sys; read = sys.stdin.readline
import heapq

n, l = map(int, read().split())
p = list(map(int, read().split()))
h = []
for i in range(n):
    heapq.heappush(h, (-(p[i]+0.5), (p[i]-0.5)))

cnt = 0
ts = 0; tf = 0
while len(h) != 0:
    f, s = heapq.heappop(h)
    f = -f
    if f <= ts:
        tf = f
        ts = tf - l
        cnt +=1
    while ts <= s and f <= tf:
        f, s = heapq.

print(h)
