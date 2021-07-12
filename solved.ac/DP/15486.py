import sys; read = sys.stdin.readline
n = int(read())
Ti = [0]; Pi = [0]
for i in range(n):
    t, p = map(int, read().split())
    Ti.append(t)
    Pi.append(p)
print(Ti)
print(Pi)
dp = [0] * (n+1)
for day in range(1, n+1):
    if day + Ti[day] -1 <= n:
        dp[day-1+Ti[day]] = max(dp[day-1+Ti[day]], dp[day-1]+Pi[day])
        print(day, Ti[day], dp, Pi[day])
    else:
        dp[day] = max(dp[day], dp[day-1])
    
print(dp)
print(dp[n-1])