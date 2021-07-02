import sys; read = sys.stdin.readline
ret = []
while True:
    h, w = map(int, read().split())
    if h == 0 and w == 0:
        break
    dp = [[0 for _ in range(w)] for __ in range(h)]
    dp[0][0] = 0; dp[0][1] = 1; dp[1][0] = 1
    while True:
        a, b = map(int, read().split())
        if a == 0 and b == 0:
            break
        dp[a][b] = 0
    for i in range(1, h):
        for j in range(1, w):
            if dp[i][j] != 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    for item in dp:
        print(item)
    ret.append(dp[h-1][w-1])    

for idx, ans in enumerate(ret):
    print(f'Map {idx+1}: {ans}')

    