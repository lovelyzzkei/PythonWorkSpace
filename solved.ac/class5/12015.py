import sys; read = sys.stdin.readline
from bisect import bisect_left

n = int(read())
a = list(map(int, read().split()))
lis = []
ans = 0
for num in a:
    if not lis:
        lis.append(num)
        ans += 1
        continue
    
    if lis[-1] < num:
        lis.append(num)
        ans += 1
    else:
        idx = bisect_left(lis, num)
        lis[idx] = num
    # print(lis, num, ans)

print(ans)