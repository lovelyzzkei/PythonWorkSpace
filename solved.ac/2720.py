import sys; read = sys.stdin.readline

t = int(read())
ret = []
for _ in range(t):
    c = int(read())
    q = c // 25; c %= 25
    r = c // 10; c %= 10
    n = c // 5; c %= 5
    ret.append(f"{q} {r} {n} {c}")
print("\n".join(x for x in ret))