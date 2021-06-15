import sys; read = sys.stdin.readline

n = int(read())
inOrder = list(map(int, read().split()))
postOrder = list(map(int, read().split()))

ret = []

def divideLeftRight(i_s, i_e, p_s, p_e):
    global ret
    
    if i_e-i_s == 1:
        ret.append(inOrder[i_s])
        return

    if i_e-i_s == 2:
        ret.append(inOrder[i_s+1])
        ret.append(inOrder[i_s])
        return 

    if inOrder[i_s:i_e] == postOrder[p_s:p_e+1]:    # 중위와 후위 순회의 배열이 동일 -> 왼쪽 가지에만 노드들 존재
        for i in range(i_e-i_s):
            ret.append(inOrder[-(i+1)])
        return 
    
    root = postOrder[p_e]
    idx = i_s
    while inOrder[idx] != root:
        idx += 1

    ret.append(root)
    divideLeftRight(i_s, idx, i_s, idx-1)
    divideLeftRight(idx+1, i_e, idx, p_e-1)

divideLeftRight(0, len(inOrder), 0, len(inOrder)-1)
print(' '.join(str(x) for x in ret))