import sys; read = sys.stdin.readline

n = int(read())

def fibo(n):
    ZERO = [[1, 0], [0, 1]]
    SIZE = 2
    BASE = [[1, 1], [1, 0]]

    def square_matrix_mul(a, b, size):
        new = [[0 for _ in range(size)] for _ in range(size)]

        # 두 2x2 정사각행렬의 곱을 구함
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    new[i][j] += (a[i][k] * b[k][j]) % 1000000007

        return new

    def get_nth(n):
        matrix = ZERO.copy()    # 기저 행렬
        k = 0
        tmp = BASE.copy()

        while 2 ** k <= n:
            # 모든 자연수는 2의 제곱수로 표현이 가능하다. 따라서 n을 구성하는 2의 제곱수를 구하고
            # 그들의 곱으로 n번째 행렬의 곱을 쉽게 구할 수 있다.
            # 이때 2**k 가 n을 구성하는지 확인하기 위해 비트마스크 사용.
            if n & (1 << k) != 0:   # 현재 2의 제곱수가 n을 구성하는 2의 제곱수
                matrix = square_matrix_mul(matrix, tmp, SIZE)
            k += 1
            tmp = square_matrix_mul(tmp, tmp, SIZE)  
        
        return matrix
    
    return get_nth(n)[1][0]

print(fibo(n)%1000000007)