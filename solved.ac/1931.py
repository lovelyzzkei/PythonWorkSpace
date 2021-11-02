import sys; read = sys.stdin.readline

n = int(read())
sch = [list(map(int, read().split())) for _ in range(n)]
sch = sorted(sch, key=lambda x:(x[1], x[0]))

# print(sch)

cnt = 0
end = 0

for i in range(n):
    if sch[i][0] >= end:
        cnt += 1
        end = sch[i][1]

print(cnt)