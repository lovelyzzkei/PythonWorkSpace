import sys; read = sys.stdin.readline

def nqueen(r):  # 각 행에 대해서 진행
    global ans
    if r == n:  # 모든 행에 조건에 맞게 퀸을 배치하였으면 종료
        ans += 1
        return
    
    for c in range(n):  # 각각의 열에 배치할 수 있는지 확인
        if col[c] or diag_l[r-c+n-1] or diag_r[r+c]:    # 현재 존재하는 위치에서 같은 열 또는 같은 대각선 상에 위치하면 x
            continue
        col[c] = diag_l[r-c+n-1] = diag_r[r+c] = True
        nqueen(r+1) # 다음 열로 진행
        col[c] = diag_l[r-c+n-1] = diag_r[r+c] = False  # 백트래킹


n = int(read())
ans = 0
col = [False]*n; diag_l = [False]*(2*n-1); diag_r = [False]*(2*n-1)
nqueen(0)
print(ans)