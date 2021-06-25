import sys; read = sys.stdin.readline
import itertools

n, m = map(int, read().split())
t = sorted(list(map(int, read().split())))
result = list(itertools.permutations(t, m))

for item in result:
    print(" ".join(str(x) for x in item))