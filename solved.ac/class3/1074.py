import sys

N, r, c = map(int, sys.stdin.readline().split())

isSearch = False

dy = [0, 0, 1, 0]
dx = [0, 1, -1, 1]

def search(N, r, c, y, x, cnt):
    global isSearch
    if isSearch:
        return 0

    if N == 1:
        for i in range(4):
            y += dy[i]; x += dx[i]
            cnt += 1
            if y == r and x == c:
                isSearch = True
                return cnt
        return cnt

    a1 = search(N-1, r, c, y, x, cnt) 
    a2 = search(N-1, r, c, y, x + pow(2, N-1), cnt)
    a3 = search(N-1, r, c, y + pow(2, N-1), x, cnt)
    a4 = search(N-1, r, c, y + pow(2, N-1), x + pow(2, N-1), cnt)
    return a1+a2+a3+a4


print(search(N, r, c, 0, 0, 0))