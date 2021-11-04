from math import floor

def crossingpoint(s, t):
    if s == t:
        return s
    mid = floor((s+t)/2)
    # print(mid)
    # if a[mid] >= b[mid] and a[mid+1] <= b[mid+1]:
    #     return mid
    if a[mid] >= b[mid]:
        return crossingpoint(mid, t)
    else:
        return crossingpoint(s, mid)

a = [8, 1]
b = [1, 8]

print(crossingpoint(0, 1))