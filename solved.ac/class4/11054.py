import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
lcs, lds = [1 for i in range(n)], [1 for i in range(n)]
for j in range(1, n):
    for i in range(j):
        if a[j] > a[i]:
            lcs[j] = max(lcs[i] + 1, lcs[j])
            
for j in range(n-1,-1,-1):
    for i in range(n-1,j,-1):
        if a[j] > a[i]:
            lds[j] = max(lds[i] + 1, lds[j])

lbs = [1 for i in range(n)]
for i in range(n):
    lbs[i] = lcs[i] + lds[i] - 1
print(max(lbs))