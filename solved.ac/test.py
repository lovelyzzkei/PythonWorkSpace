import sys; read = sys.stdin.readline
import itertools

# 분할 정복
def cul_sum(i, j):
    return (list(itertools.accumulate(nums[i:j+1]))[-1])

ret = []
n, m = map(int, read().split())
nums = [0] + list(map(int, read().split()))
cul_nums = list(itertools.accumulate(nums))
for _ in range(m):
    i, j = map(int, read().split())
    ret.append(cul_nums[j] - cul_nums[i-1])

print('\n'.join(str(x) for x in ret))