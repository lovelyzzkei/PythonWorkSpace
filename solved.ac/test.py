import collections
import sys; read=sys.stdin.readline

colorPaper = []     # 색종이를 저장할 배열

N = int(read())
for i in range(N):
    colorPaper.append(list(map(int, read().split())))
print(colorPaper)