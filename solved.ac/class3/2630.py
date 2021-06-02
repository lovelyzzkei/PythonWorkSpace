import sys

N = int(sys.stdin.readline())
colorPaper = []
paper_blue = 0
paper_white = 0

# 색종이 배열 생성
for i in range(N):
    colorPaper.append(list(map(int, sys.stdin.readline().strip().split())))


# 분할 정복으로 해결
def checkUniform(N, y, x):
    global paper_white, paper_blue

    sub_paper = [col[x:x+N] for col in colorPaper[y:y+N]]
        
    if all(all(x) for x in sub_paper):     # 파란색
        paper_blue += 1
        return
    if any(any(x) for x in sub_paper) == False:    # 하얀색
        paper_white += 1
        return
    
    checkUniform(N//2, y, x)                  # 왼쪽 위
    checkUniform(N//2, y, x + N//2)         # 오른쪽 위
    checkUniform(N//2, y + N//2, x)         # 왼쪽 아래
    checkUniform(N//2, y + N//2, x + N//2)# 오른쪽 아래

    return

checkUniform(N, 0, 0)
print(paper_white)
print(paper_blue)