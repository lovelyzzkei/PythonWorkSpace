import sys; read = sys.stdin.readline
T = int(read())
ret = []
for t in range(T):
    front_c = [0] * 16  # 앞이 자음
    front_v = [0] * 16  # 앞이 모음
    c, v, l = map(int, read().split())
    front_v[1] = v
    for i in range(2, l+1):
        front_c[i] = (c*front_v[i-1]) % 1000000007
        front_v[i] = (v*front_v[i-1] + v*front_c[i-1]) % 1000000007
    ret.append((front_c[l]+front_v[l])% 1000000007)
    
for i, ans in enumerate(ret):  
    print(f"Case #{i+1}: {ans}")
