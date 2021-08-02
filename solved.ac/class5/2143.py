import sys; read = sys.stdin.readline
from itertools import combinations

T = int(read())
n = int(read())
a = list(map(int, read().split()))
pSumA = [0] * (n+1)
for i in range(1, n+1):
    pSumA[i] = pSumA[i-1] + a[i-1]

retA = []
for i in range(1, n+1):
    for j in range(i):
        retA.append(pSumA[i] - pSumA[j])
retA = sorted(list(set(retA)))

m = int(read())
b = list(map(int, read().split()))
pSumB = [0] * (m+1)
for i in range(1, m+1):
    pSumB[i] = pSumB[i-1] + b[i-1]

retB = []
for i in range(1, m+1):
    for j in range(i):
        retB.append(pSumB[i] - pSumB[j])
retB = sorted(list(set(retB)))
print(retA)
print(retB)

ptr1 = 0; ptr2 = 0
ans = 0 
while ptr1 < len(retA) and ptr2 < len(retB):
    partial_sum = retA[ptr1] + retB[ptr2]
    if partial_sum == T:
        ans += 1
        ptr2 += 1
    elif partial_sum < T:
        if retA[ptr1] < retB[ptr2]:
            ptr1 += 1
        else:
            ptr2 += 1
    else:
        if retA[ptr1] < retB[ptr2]:
            ptr2 -= 1
        else:
            ptr1 -= 1

print(ans)