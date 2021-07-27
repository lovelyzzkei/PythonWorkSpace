import sys; read = sys.stdin.readline

n = int(read())
a = [0] + list(map(int, read().split()))
lis = {i:1 for i in range(1, n+1)}

def binary_search(start, end, target):
    tmp = sorted(list(set(a[start:end])))
    left = 0; right = len(tmp)-1
    while left <= right:
        mid = (left + right) // 2
        if tmp[mid] == target:
            return mid
        elif tmp[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    if left > right:
        return left
    else:
        return right


for i in range(2, n+1):
    lis[i] += binary_search(1, i, a[i])

print(max(lis.values()))