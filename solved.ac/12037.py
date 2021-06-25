import sys; read = sys.stdin.readline
MAX_RANGE = 16
t = int(read())
dp = [0]*MAX_RANGE; dp[0] = 1; dp[1] = 1
def fibo():
    for i in range(2, MAX_RANGE):
        dp[i] = dp[i-1] + dp[i-2]

fibo()
for i in range(t):
    c, v, l = map(int, read().split())
    print(f"Case #{i+1}: {dp[l]}")
