import sys; read = sys.stdin.readline

a = int(read())
b, c = map(int, read().split())
s = read().strip()
ret = [a+b+c, s]
print(' '.join(str(x) for x in ret))