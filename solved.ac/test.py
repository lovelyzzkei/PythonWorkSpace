import sys; read = sys.stdin.readline
import psutil

n = int(read())
inOrder = list(map(int, read().split()))
postOrder = list(map(int, read().split()))

ret = []

def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.5f} MB")

def divideLeftRight(inOrder, postOrder):
    global ret

    if inOrder == postOrder:    # 중위와 후위가 같을 경우는 노드가 모두 왼쪽 가지에만 있다는 것
        for i in range(len(inOrder)):
            ret.append(inOrder[-(i+1)])
        return

    if len(inOrder) == 1:
        ret += [inOrder[0]]
        return
    if len(inOrder) == 2:
        ret += [inOrder[1]]
        ret += [inOrder[0]]
        return
    
    root = postOrder[-1]
    idx = 0
    while inOrder[idx] != root:
        idx += 1

    in_left = inOrder[:idx]; in_right = inOrder[idx+1:]
    post_left = postOrder[:idx]; post_right = postOrder[idx:-1]

    ret.append(root)
    divideLeftRight(in_left, post_left)
    divideLeftRight(in_right, post_right)


divideLeftRight(inOrder, postOrder)
print(' '.join(str(x) for x in ret))