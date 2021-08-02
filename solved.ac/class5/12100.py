import sys; read = sys.stdin.readline

n = int(read())
board = [list(map(int, read().split())) for i in range(n)]
ret = []

def dfs(*board):
    s = [[board, 0]]

    while s:
        now, move = s.pop()
        if move == 5:
            ret.append(max(max(x for x in now)))
            continue
        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            
