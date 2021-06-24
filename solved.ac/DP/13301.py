import sys; read = sys.stdin.readline
fibo = [0] * 81; fibo[1] = 1
for i in range(2, 81):
    fibo[i] = fibo[i-1] + fibo[i-2]
input = int(read())
h = fibo[input]; w = fibo[input] + fibo[input-1]
print(2*(h+w))