import sys; read = sys.stdin.readline
n = int(read())
c = read().strip()
i = 0; count = 0
while i < n:
    if c[i:i+4] == 'pPAp':
        count += 1
        i += 4
    else:
        i += 1
print(count)