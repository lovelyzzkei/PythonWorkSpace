import sys; read = sys.stdin.readline
n, m = map(int, read().split())
nums = sorted(list(map(int, read().split())))
def permute(nums):
    results = []
    prev_elements = []
    def dfs(nums):
        if len(prev_elements) == m:
            results.append(prev_elements[:])
            return
        for e in nums:
            next_elements = nums[:]
            next_elements.remove(e)
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    # 중복되는 수열을 제거하기 위한 튜플 및 set 작업
    results = list(map(tuple, results))
    return sorted(list(set(results)))

ret = permute(nums)
for item in ret:
    print(' '.join(str(x) for x in item))
