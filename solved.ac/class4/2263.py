import sys; read = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(read())
inOrder = list(map(int, read().split()))
postOrder = list(map(int, read().split()))

ret = []

def divideLeftRight(i_s, i_e, p_s, p_e):
    global ret

    if i_e-i_s == 0:    # 한쪽 가지가 비어있는 경우
        return

    if i_e-i_s == 1:
        ret.append(inOrder[i_s])
        return
    
    root = postOrder[p_e]
    idx = i_s
    while True:     # 양쪽에서 탐색을 하며 시간 반으로 줄임
        if inOrder[idx] == root:
            break
        elif inOrder[i_e-idx-1] == root:
            idx = i_e-idx-1
            break
        idx += 1

    ret.append(root)
    divideLeftRight(i_s, idx, p_s, p_s+(idx-i_s)-1)
    divideLeftRight(idx+1, i_e, p_s+(idx-i_s), p_e-1)

divideLeftRight(0, len(inOrder), 0, len(inOrder)-1)
print(' '.join(str(x) for x in ret))    
