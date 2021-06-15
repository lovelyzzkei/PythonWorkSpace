import sys; read = sys.stdin.readline

n = int(read())
a, b, c = map(int, read().split())
dp = [[a, a], [b, b], [c, c]]   # 처음 세 개의 값으로 dp배열 초기화

for _ in range(n-1):
    a, b, c = map(int, read().split())
    v1, v2, v3 = [item[:] for item in dp]        # 깊은 복사

    # 각 단계마다 최댓값
    dp[0][0] = max(v1[0], v2[0]) + a
    dp[1][0] = max(v1[0], v2[0], v3[0]) + b
    dp[2][0] = max(v2[0], v3[0]) + c

    # 각 단계마다 최솟값
    dp[0][1] = min(v1[1], v2[1]) + a
    dp[1][1] = min(v1[1], v2[1], v3[1]) + b
    dp[2][1] = min(v2[1], v3[1]) + c

print(max(x[0] for x in dp), min(x[1] for x in dp))