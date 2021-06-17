import sys; read = sys.stdin.readline

n = int(read())

for i in range(n):
    print(' '*((2*(n-i)-1)//2) + '*'*(2*i+1))

for i in range(n-2, -1, -1):
    print(' '*((2*(n-i)-1)//2) + '*'*(2*i+1))