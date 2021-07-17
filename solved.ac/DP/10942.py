import sys; read = sys.stdin.readline
n = int(read())
dp = [[0 for _ in range(n+1)] for __ in range(n+1)]
t = [0] + list(map(int, read().split()))

# 자기 자신은 펠린드롬
for i in range(n+1):
    dp[i][i] = 1

# 길이를 1씩 증가해가며 펠린드롬 확인
# 앞 뒤가 동일하고, 그 안에 있는 문자열이 이미 펠린드롬이면, 앞 뒤 수를 붙인 것도 펠린드롬
for len in range(1, n):
    for i in range(1, n-len+1): 
        if len == 1 and t[i] == t[i+len]:   # 길이가 2인 문자열은 따로 처리
            dp[i][i+len] = 1
        elif t[i] == t[i+len] and dp[i+1][i+len-1]:
            dp[i][i+len] = 1

m = int(read())
ret = []
for _ in range(m):
    s, e = map(int, read().split())
    ret.append(dp[s][e])
print('\n'.join(str(x) for x in ret))