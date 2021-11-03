import sys; read = sys.stdin.readline
import heapq

n = int(read())
lec = [list(map(int, read().split())) for i in range(n)]
lec = sorted(lec, key=lambda x:(x[0], x[1]))

# print(lec)

room = [0]

for s, t in lec:
    if room[0] > s:
        heapq.heappush(room, t)
    else:
        heapq.heappop(room)
        heapq.heappush(room, t)


print(len(room))