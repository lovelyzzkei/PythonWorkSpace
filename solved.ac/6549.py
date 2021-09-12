import sys; read = sys.stdin.readline

def maxHistogram(start, end):
    if start == end:
        return a[start]
    mid = (start + end) // 2
    # 왼쪽과 오른쪽 영역에서의 최대 히스토그램 영역
    ret = max(maxHistogram(start, mid), maxHistogram(mid+1, end))
    # 최대 히스토그램이 반으로 나눈 경계를 포함하는 경우
    lo = mid; hi = mid+1
    height = min(a[lo], a[hi])
    ret = max(ret, height*2)
    while (start < lo or hi < end):
        if hi < end and (lo == start or a[lo-1] < a[hi+1]):
            hi += 1
            height = min(height, a[hi])
        else:
            lo -= 1
            height = min(height, a[lo])

        ret = max(ret, height * (hi-lo+1))
    return ret
        

ans = []
while True:
    input = list(map(int, read().split()))
    if input[0] == 0:
        break
    n = input[0]; a = input[1:]
    ans.append(maxHistogram(0, n-1))
print('\n'.join(str(x) for x in ans))