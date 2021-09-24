import sys; read = sys.stdin.readline
MIN = 0

n = int(read())
a = list(map(int, read().split()))

def maxSubArray(s, e):
    if s == e:
        return a[s]**2
    mid = (s+e) // 2
    ans = max(maxSubArray(s, mid), maxSubArray(mid+1, e))
    lo = mid; hi = mid; 
    base = a[lo]; height = a[lo]
    ret = base*height
    while s<lo or hi<e:
        if hi<e and (lo==s or a[lo-1]<a[hi+1]):
            hi += 1
            base +=a[hi]
            height = min(height, a[hi])
        else:
            lo -= 1
            base += a[lo]
            height = min(height, a[lo])
        ret = max(ret, base*height)
    return max(ans, ret)


print(maxSubArray(0, n-1))