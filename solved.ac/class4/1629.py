import sys; read = sys.stdin.readline

dp = [1] * 2_147_483_647 

def multiply(a, b, c):
    if b == 1:
        dp[b] = a % c
    if dp[b] == 1:
        dp[b] = (multiply(a, b//2, c) % c) * (multiply(a, b-b//2, c) % c)
    return dp[b]


a, b, c = map(int, read().split())
print(multiply(a, b, c))