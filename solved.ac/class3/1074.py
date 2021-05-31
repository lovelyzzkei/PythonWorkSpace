import sys

N, r, c = map(int, sys.stdin.readline().split())

N = 2 ** N
ans = 0

dy = [0, 0, 1, 1]
dx = [0, 1, 0, 1]

# r행 c열이 있는 2 x 2 사각형을 찾아서 그 안에서 해당 행열이 몇번쨰인지 확인
# 나머지 사각형은 다 날림
# 사각형을 4등분하여 r행 c열이 존재하는 부분만 살리고 나머지는 모두 버림
# 필요한 부분만 분할 정복!!
while N > 2:
    if N // 2 > r: # 위
        if N // 2 <= c:     # 오른
            ans += pow(N // 2, 2)
            c -= N // 2
    
    else:   # 아래
        r -= N // 2
        if N // 2 <= c:     # 오른
            ans += 3 * pow(N // 2, 2)
            c -= N // 2
        else:    # 왼쪽
            ans += 2 * pow(N // 2, 2)
    
    N //= 2

for i in range(4):
    if r == dy[i] and c == dx[i]:
        print(ans)
        break
    ans += 1