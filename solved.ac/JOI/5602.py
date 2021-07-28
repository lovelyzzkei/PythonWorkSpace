import sys; read = sys.stdin.readline

n, m = map(int, read().split())
total = {i:0 for i in range(1, m+1)}
for i in range(n):
    input = list(map(int, read().split()))
    for i, v in enumerate(input):
        total[i+1] += v

total = sorted(total.items(), key=lambda x:x[1], reverse=True)
print(' '.join(str(x[0]) for x in total))