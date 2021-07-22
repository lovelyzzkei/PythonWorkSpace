import sys; read = sys.stdin.readline

ANSWER = [1, 2, 3, 4, 5, 6, 7, 8, 9]
MAP = [list(map(int, read().split())) for i in range(9)]
missing_row = []; missing_col = []; subgrid = []

# 각 열과 행에 아직 채워지지 않은 숫자 찾아놓기
for row in range(9):
    missing_row.append({i:True for i in range(1, 10)})
    for x in ANSWER:
        if x not in MAP[row]:
            missing_row[row][x] = False

for col in range(9):
    tmp = []
    for row in range(9):
        tmp.append(MAP[row][col])
    missing_col.append({i:True for i in range(1, 10)})
    for x in ANSWER:
        if x not in tmp:
            missing_col[col][x] = False

# 3x3 배열에 없는 숫자 찾아놓기
for row in range(3):
    for col in range(3):
        tmp = [x[3*col:3*(col+1)] for x in MAP[3*row:3*(row+1)]]
        t = []
        for i in range(3):
            for j in range(3):
                t.append(tmp[i][j])
        subgrid.append({i:True for i in range(1, 10)})
        for x in ANSWER:
            if x not in t:
                subgrid[3*row+col][x] = False

# print(missing_row)
# print(missing_col)
# print(subgrid)

def isValid(row, x, notFill):
    if not missing_row[row][notFill] and \
        not missing_col[x][notFill] and \
        not subgrid[3*(row//3)+(x//3)][notFill]:

        missing_row[row][notFill] = True
        missing_col[x][notFill] = True
        subgrid[3*(row//3)+(x//3)][notFill] = True
        return True
        
    else:
        return False


def sudoku(row):
    if row == 9:
        print('\n'.join(x for x in [' '.join(str(x) for x in row) for row in MAP]))
        return

    notFills = []
    for i in range(1, 10):
        if not missing_row[row][i]:
            notFills.append(i)
     
    for notFill in notFills:

        # 해당 row에서 빈칸인 x좌표를 구함
        tmp = []
        for x in range(9):
            if MAP[row][x] == 0:
                tmp.append(x)

        # print(row, notFill, tmp)
        for x in tmp:
            if isValid(row, x, notFill):
                MAP[row][x] = notFill
                if all(list(missing_row[row].values())):  # 해당 row를 다 채웠으면 다음 row로 넘어감
                    sudoku(row+1)
                    MAP[row][x] = 0
sudoku(0)