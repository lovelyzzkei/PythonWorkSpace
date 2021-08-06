import sys; read = sys.stdin.readline

n = int(read())
k = int(read())

b = []
for i in range(1, n+1):
    for j in range(1, n+1):
        b.append(i*j)
    
print(b)