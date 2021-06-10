import sys; read = sys.stdin.readline
from collections import deque

# def bfs(n):
#     dq = deque([n])
#     oper = 0

#     while dq:
#         qlen = len(dq)
#         while qlen:
#             cur = dq.popleft()
#             if cur == 1:
#                 return oper

#             if cur % 3 == 0: dq.append(cur // 3)
#             if cur % 2 == 0: dq.append(cur // 2)
#             dq.append(cur-1)
        
#             qlen -= 1
#         oper += 1


n = int(read())
dp = [10000001] * (n+1)
dp[n] = 0

for i in range(n, 1, -1):
    if i % 3 == 0: 
        dp[i//3] = min(dp[i] + 1, dp[i//3])
    if i % 2 == 0:
        dp[i//2] = min(dp[i] + 1, dp[i//2])
    dp[i-1] = min(dp[i] + 1, dp[i-1])

print(dp[1])
# print(bfs(n))