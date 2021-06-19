import sys; read = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(read())
inOrder = list(map(int, read().split()))
postOrder = list(map(int, read().split()))

# 루트 노드 이전의 노드의 개수를 미리 저장하여 재귀 함수 내에서 사용!
pos = [0] * (n+1)
for i in range(n):
    pos[inOrder[i]] = i

ret = []

def preOrder(i_s, ie, ps, pe):
    if i_s == ie:
        return
    
    root = postOrder[pe-1]
    ret.append(root)
    idx = pos[root] - i_s

    preOrder(i_s, i_s+idx, ps, ps+idx)
    preOrder(i_s+idx+1, ie, ps+idx, pe-1)

preOrder(0, len(inOrder), 0, len(inOrder))
print(' '.join(str(x) for x in ret))    
