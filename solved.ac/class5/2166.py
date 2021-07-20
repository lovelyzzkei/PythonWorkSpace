import sys; read = sys.stdin.readline

n = int(read())
coor = []
first = list(map(int, read().split()))
coor.append(first)
for tc in range(n-1):
    coor.append(list(map(int, read().split())))
coor.append(first)

sum_xy = 0; sum_yx = 0
for x in range(n):
    sum_xy += (coor[x][0] * coor[x+1][1])
    sum_yx += (coor[x][1] * coor[x+1][0])

ans = (sum_xy-sum_yx) / 2
print(round(abs(ans), 2))