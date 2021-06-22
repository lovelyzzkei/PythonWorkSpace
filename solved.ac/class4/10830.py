import sys; read = sys.stdin.readline

size, b = map(int, read().split())
a = [list(map(int, read().split())) for j in range(size)]

def square_matrix_mul(a, b, size):
    new = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                new[i][j] += (a[i][k] * b[k][j]) % 1000
    
    return new

def get_nth(n):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        matrix[i][i] = 1

    tmp = a.copy()
    k = 0
    
    while 2 ** k <= n:
        if n & (1 << k) != 0:
            matrix = square_matrix_mul(matrix, tmp, size)
        k += 1
        tmp = square_matrix_mul(tmp, tmp, size)

    return matrix

ans = get_nth(b)
for i in range(size):
    for j in range(size):
        print(ans[i][j] % 1000, end=" ")
    print()