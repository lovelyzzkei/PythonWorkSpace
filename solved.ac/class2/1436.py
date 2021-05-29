import sys

n = int(sys.stdin.readline().strip())
movie = 666

# 어이가 없다 진짜...
while n:
    if "666" in str(movie):
        n -= 1
    movie += 1

print(movie - 1)