import sys; read = sys.stdin.readline
n, k = map(int, read().split())
a = []
pSum = [0] * (n+1)
for tc in range(n):
    a.append(int(read()))

for i in range(n):
    pSum[i+1] = pSum[i] + a[i]

ans = 0
for i in range(k, n+1):
    ans = max(ans, pSum[i]-pSum[i-k])
print(ans)

print(a)
print(pSum[:n+1])