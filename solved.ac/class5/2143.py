import sys; read = sys.stdin.readline
from bisect import bisect_left, bisect_right

T = int(read())
n = int(read())
a = list(map(int, read().split()))
pSumA = [0] * (n+1)
for i in range(1, n+1):
    pSumA[i] = pSumA[i-1] + a[i-1]

retA = {}
for i in range(1, n+1):
    for j in range(i):
        pSum = pSumA[i] - pSumA[j]
        try:
            retA[pSum] += 1
        except:
            retA[pSum] = 1

m = int(read())
b = list(map(int, read().split()))
pSumB = [0] * (m+1)
for i in range(1, m+1):
    pSumB[i] = pSumB[i-1] + b[i-1]

retB = []
for i in range(1, m+1):
    for j in range(i):
        retB.append(pSumB[i] - pSumB[j])
retB = sorted(retB)
# print(retA)
# print(retB)

ans = 0
for key in retA.keys():
    ans += retA[key] * (bisect_right(retB, T-key) - bisect_left(retB, T-key))

print(ans)