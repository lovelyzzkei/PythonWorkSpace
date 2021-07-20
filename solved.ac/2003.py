import sys; read = sys.stdin.readline
n, m = map(int, read().split())
t = [0] * (10001)
t[:n] = list(map(int, read().split())).copy()
ans = 0
start = 0; end = 0; sum = 0

while end <= n and start <= end:
    if sum >= m:
        sum -= t[start]
        start += 1
    elif sum < m:
        sum += t[end]
        end += 1
    if sum == m:
        ans += 1
print(ans)