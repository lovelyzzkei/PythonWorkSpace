import sys; read = sys.stdin.readline
from math import sqrt
from bisect import bisect_left, bisect_right

n = int(read())
#[[x1, y1], [x2, y2], .., [xn, yn]]
c = [list(map(int, read().split())) for i in range(n)]  
# 먼저 x좌표를 기준으로 정렬
c = sorted(c, key = lambda x:x[0])
def d(a, b):
    return pow(c[a][0]-c[b][0], 2) + pow(c[a][1]-c[b][1], 2)

def binary_search(s, e, t):
    while s <= e:
        mid = (s+e)//2
        if c[mid][0] == t:
            return mid
        elif c[mid][0] > t:
            e = mid - 1
        else:
            s = mid + 1
    return s

def closestPair(s, e):
    if e-s <= 2:    # 3개의 점 -> 모두 enumerate
        ret = sys.maxsize
        for i in range(s, e):
            for j in range(i+1, e+1):
                ret = min(ret, d(i, j))
        return ret

    mid = (s+e)//2; x_mid = c[mid][0]
    dl = closestPair(s, mid)
    dr = closestPair(mid+1, e)

    delta = min(dl, dr);
    ms = binary_search(s, e, x_mid-int(sqrt(delta)))
    me = binary_search(s, e, x_mid+int(sqrt(delta)))
    s = sorted(c[ms:me+1][:], key=lambda x:x[1])    # y좌표를 기준으로 sort
    tmp = sys.maxsize
    for i in range(len(s)):
        for j in range(i+1, i+5):
            if 0 <= i and j < len(s):
                dist = pow(s[i][0]-s[j][0], 2) + pow(s[i][1]-s[j][1], 2)
                tmp = min(tmp, dist)
    return min(tmp, delta)

print(closestPair(0, n-1))