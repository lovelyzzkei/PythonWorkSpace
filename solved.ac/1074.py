import sys; read = sys.stdin.readline

n, r, c = map(int, read().split())
cnt = 0

def z_search(n, r, c, rs, cs):
    global cnt
    if n == 2:
        if r-rs==1: cnt += 2
        if c-cs==1: cnt += 1
        return cnt
    
    if rs<=r<rs+n//2 and cs<=c<cs+n//2: # 제 1영역
        return z_search(n//2, r, c, rs, cs)
    elif rs<=r<rs+n//2 and cs+n//2<=c<cs+n: # 제 2영역
        cnt += pow(n//2, 2)
        return z_search(n//2, r, c, rs, cs+n//2)
    elif rs+n//2<=r<rs+n and cs<=c<cs+n//2: # 제 3영역
        cnt += 2 * pow(n//2, 2)
        return z_search(n//2, r, c, rs+n//2, cs)
    else: # 제 4영역
        cnt += 3 * pow(n//2, 2)
        return z_search(n//2, r, c, rs+n//2, cs+n//2)

print(z_search(2**n, r, c, 0, 0))