import sys; read = sys.stdin.readline

s = read().strip()

zero = [v for v in s.split('0') if v]
one = [v for v in s.split('1') if v]

print(min(len(zero), len(one)))