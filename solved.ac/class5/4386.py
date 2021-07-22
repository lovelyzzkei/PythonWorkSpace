import sys; read = sys.stdin.readline
from math import sqrt, pow

n = int(read())
INF = int(1e4)
MAP = [[INF for _ in range(n)] for __ in range(n)]
stars = []
for tc in range(n):
    stars.append(list(map(float, read().split())))

for i in range(n):
    for j in range(i):
        star1 = stars[i]; star2 = stars[j]
        dist = sqrt(pow(star1[0]-star2[0], 2)+pow(star1[1]-star2[1], 2))
        MAP[i][j] = dist
        MAP[j][i] = dist
    
for mid in range(n):
    for start in range(n):
        for end in range(n):
            if MAP[start][mid] + MAP[mid][end] < MAP[start][end]:
                MAP[start][end] = MAP[start][mid] + MAP[mid][end]

for item in MAP:
    print(item)