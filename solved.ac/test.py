def binary_search(s, e, t):
    if s > e:
        return s
    mid = (s+e)//2
    if c[mid] == t:
        return mid
    elif c[mid] > t:
        e = mid - 1
    else:
        s = mid + 1
    return binary_search(s, e, t)

c = [1, 2, 3, 4, 6, 7, 8]
print(binary_search(0, len(c)-1, 5))
print(c[0:8])