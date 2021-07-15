import sys; read = sys.stdin.readline
n, m = map(int, read().split())
a = list(map(int, read().split()))
c = list(map(int, read().split()))

# 각 리스트의 누적 합 리스트 생성
cul_a = [0] * (n+1)
cul_c = [0] * (n+1)
for i in range(1, n+1):
    cul_a[i] = cul_a[i-1] + a[i-1]
    cul_c[i] = cul_c[i-1] + c[i-1]

# print(cul_a)
# print(cul_c)

# 앱을 1개 종료 ~ 모두 종료하며 확보되는 메모리와 비용의 최솟값 저장
dp = {}
for len in range(1, n+1):
    for i in range(len, n+1):
        tar = cul_a[i] - cul_a[i-len]
        try:
            dp[tar] = min(dp[tar], cul_c[i] - cul_c[i-len])
        except:
            dp[tar] = cul_c[i] - cul_c[i-len]

while True:
    try: 
        print(dp[m])
        break
    except:
        m += 1