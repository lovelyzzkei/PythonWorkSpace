import sys; read = sys.stdin.readline

t = int(read())

a = 0; b = 0; c = 0

while t >= 10:
    if t >= 300:
        a += t // 300
        t %= 300
    elif t >= 60:
        b += t // 60
        t %= 60
    else :
        c += t // 10 
        t %= 10
    
if t != 0:
    print(-1)
else :
    print(a, b, c)