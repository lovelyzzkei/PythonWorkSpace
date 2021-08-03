import bisect

a = [1, 2, 2, 3, 4]
print(bisect.bisect_left(a, 8))
print(bisect.bisect_right(a, 8))