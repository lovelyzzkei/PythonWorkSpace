import sys; read = sys.stdin.readline
n, m = map(int, read().split())
nums = sorted(list(set(list(map(int, read().split())))))
def permute(nums):
    results = []
    prev_elements = []
    def dfs(nums):
        if len(prev_elements) == m:
            results.append(prev_elements[:])
            return
        for i, v in enumerate(nums):
            next_elements = nums[i:]
            prev_elements.append(v)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results
ret = permute(nums)
for item in ret:
    print(" ".join(str(x) for x in item))