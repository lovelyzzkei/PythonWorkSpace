import sys; read = sys.stdin.readline
k = int(read())
fibo = [0] * (k+2)
fibo[1] = 1; fibo[2] = 1
for i in range(3, k+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[k-1], fibo[k])