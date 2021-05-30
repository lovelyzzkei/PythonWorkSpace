import sys

_ = int(sys.stdin.readline())
N = sorted(map(int, sys.stdin.readline().strip().split()))
_ = int(sys.stdin.readline())
M = map(int, sys.stdin.readline().strip().split())

def binary(target, N, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if target == N[mid]:
        return N[start:end+1].count(target)
    elif target < N[mid]:
        return binary(target, N, start, mid - 1)
    else:
        return binary(target, N, mid+1, end)

n_dic = {}
for n in N:
    start = 0
    end = len(N) - 1
    if n not in n_dic:
        n_dic[n] = binary(n, N, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M))

