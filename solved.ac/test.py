a = [[4, 3], [2, 1]]
b = [[4, 3], [2, 1]]
c = [[4, 3], [2, 1]]

n=0

while n < 3:
    for i in range(0, 2):
        for j in range(0, 2):
            c[i][j] = b[i][0]*a[0][j] + b[i][1]*a[1][j]
    
    b  = [[c[i][j] for j in range(2)] for i in range(2)]
    n += 1
    print(b)

print(b)
