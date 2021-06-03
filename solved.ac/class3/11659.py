import sys; read = sys.stdin.readline

# 분할 정복
def cul_sum(i, j):
    if i == j:
        return nums[i]
    sum_ = cul_sum(i, (i+j)//2) + cul_sum((i+j)//2+1, j)
    return sum_

ret = []
n, m = map(int, read().split())
nums = {idx+1:value for idx, value in enumerate(list(map(int, read().split())))}
for _ in range(m):
    i, j = map(int, read().split())
    ret.append(cul_sum(i, j))

print('\n'.join(str(x) for x in ret))