import sys; read = sys.stdin.readline
n, s = map(int, read().split())
start = end = 0    # 투 포인터 설정
partial_sum = 0    # 부분합 parameter 설정
len = int(1e7)
t = [0] * (100001)
t[:n] = list(map(int, read().split())).copy()

while end <= n and start <= end:
    if partial_sum >= s:
        len = min(len, end - start)
        partial_sum -= t[start]
        start += 1
    else:
        partial_sum += t[end]
        end += 1

if len == int(1e7):
    print(0)
else:
    print(len)