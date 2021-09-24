import sys; read = sys.stdin.readline
MAX_WIDTH = 32768   #2**15

z = [[0 for i in range(MAX_WIDTH)] for j in range(MAX_WIDTH)]
n, r, c = map(int, read().split())
cnt = 0

def z_search(n, r, c):
    global cnt
    if n == 2:
        z[r][c] = cnt
        z[r][c+1] = cnt + 1
        z[r+1][c] = cnt + 2
        z[r+1][c+1] = cnt + 3
        cnt += 4

    z_search(n//2, r, c)
    z_search(n//2, r, c+n//2)
    z_search(n//2, r+n//2, c)
    z_search(n//2, r+n//2, c+n//2)

z_search(2**n, 0, 0)
print(z[r][c])
