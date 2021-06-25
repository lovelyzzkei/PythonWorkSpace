import sys; read = sys.stdin.readline
n, m = map(int, read().split())
nums = sorted(list(map(int, read().split())))

def permute(nums):
    results = []
    prev_elements = []
    def dfs(elements):
        if len(prev_elements) == m:
            results.append(prev_elements[:])
            return
        for i, v in enumerate(elements):
            next_elements = elements[i:]
            prev_elements.append(v)
            dfs(next_elements)
            prev_elements.pop()
    dfs(nums)
    return results

results = permute(nums)
for item in results:
    print(" ".join(str(x) for x in item))