import sys; read = sys.stdin.readline

a, b = map(int, read().split())
if a <= b and b <= a * 6:
    print("Yes")
else:
    print("No")