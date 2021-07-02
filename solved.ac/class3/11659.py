# import sys; read = sys.stdin.readline

# # 분할 정복
# def cul_sum(i, j):
#     if i == j:
#         return nums[i]
#     sum_ = cul_sum(i, (i+j)//2) + cul_sum((i+j)//2+1, j)
#     return sum_

# ret = []
# n, m = map(int, read().split())
# nums = {idx+1:value for idx, value in enumerate(list(map(int, read().split())))}
# for _ in range(m):
#     i, j = map(int, read().split())
#     ret.append(cul_sum(i, j))

# print('\n'.join(str(x) for x in ret))


import sys; read = sys.stdin.readline
n, m = map(int, read().split())
a = list(map(int, read().split()))
pSum = [0] * (n+1)
for i in range(n):
    pSum[i+1] = pSum[i] + a[i]
ret = []
for t in range(m):
    u, v = map(int, read().split())
    ret.append(pSum[v]-pSum[u-1])
print('\n'.join(str(x) for x in ret))