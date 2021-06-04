import sys;read = sys.stdin.readline

map = []
ret = 0
n, m = int(read())
for _ in range(n):
    map.append(list(map(int, read().strip().split())))

# 정사각형 2개를 가로로 붙힌 상태에서 만들 수 있는 테트로미노에 대해 합 도출
for i in range(n-1):
    for j in range(m-1):
        ret = []
        basic = map[i][j] + map[i][j+1] + map[i+1][j]
        if i + 2 < n:
            ret.append(basic+map[i+2][j])
        if j > 0:



