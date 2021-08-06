import sys; read = sys.stdin.readline

n = int(read())
a = list(map(int, read().split()))
ans = [-1]; nge = []; nge.append(a.pop())
while a:
    now = a.pop()
    while nge:
        tmp = nge.pop()
        if tmp > now:
            ans.append(tmp)
            nge.append(tmp)
            nge.append(now)
            break
    if len(nge) == 0:
        nge.append(now)
        ans.append(-1)
print(' '.join(str(x) for x in reversed(ans)))