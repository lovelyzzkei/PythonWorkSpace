import sys; read = sys.stdin.readlines
sys.setrecursionlimit(10**6)

def preToPost(start, end):
    if start == end:
        return

    root = tree[start]
    ret.append(root)
    idx = start + 1
    while idx < end and tree[idx] < root:
        idx += 1
    preToPost(idx, end)
    preToPost(start + 1, idx)


tree = []; ret = []
lines = read()
for line in lines:
    tree.append(int(line.strip()))

preToPost(0, len(tree))
for node in reversed(ret):
    print(node)