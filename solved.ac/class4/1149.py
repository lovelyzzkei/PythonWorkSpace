import sys; read = sys.stdin.readline

def dp(n):
    for i in range(1, n):
        rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
        rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
        rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]
    
    return min(rgb[n-1][0], rgb[n-1][1], rgb[n-1][2])

rgb = []
n = int(read())
for i in range(n):
    rgb.append(list(map(int, read().split())))

print(dp(n))