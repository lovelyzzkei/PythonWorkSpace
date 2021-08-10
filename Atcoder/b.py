import sys; read = sys.stdin.readline

fac = [1] * 11
for i in range(1, 11):
    fac[i] = i * fac[i-1]

# print(fac)
p = int(read())
dp = [0] * (int(1e7)+1)
facLessThanMe = [fac[10]] * (int(1e7)+1)
dp[1] = 1

for i in range(1, 10):
    for j in range(fac[i], fac[i+1]):
        facLessThanMe[j] = fac[i]



for i in range(2, p+1):
    # print(bisect_right(fac, i))
    dp[i] = dp[i-facLessThanMe[i]] + 1
print(dp[p])