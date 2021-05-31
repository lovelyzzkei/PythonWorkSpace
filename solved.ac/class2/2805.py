import sys

N, M = map(int, sys.stdin.readline().split())
woods = list(map(int, sys.stdin.readline().strip().split()))

def sum_woods(h):
    sum = 0
    for wood in woods:
        if wood >= h:
            sum += (wood - h)
    return sum

def binary(M, start, end):
    while start <= end:
        mid = (start + end) // 2
        if sum_woods(mid) < M:
            end = mid - 1
        else:
            start = mid + 1
        
    return end

print(binary(M, 0, max(woods)))
