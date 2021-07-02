import sys; read = sys.stdin.readline
a, b = map(int, read().split())
dist = 1
while True:
    hasChild = False
    if b == a:
        break
    if b % 10 == 1: # 끝자리가 1일 경우(홀수) 10으로 나누기
        b //= 10
        hasChild = True
    elif b % 2 == 0:    # 짝수일 경우
        b //= 2
        hasChild = True

    if b < a or not hasChild:
        print(-1)
        exit(0)
    dist += 1

print(dist)
    