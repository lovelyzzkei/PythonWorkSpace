import sys

N = int(sys.stdin.readline())

video = []
for _ in range(N):
    a = []
    part = sys.stdin.readline().strip()
    for i in range(N):
        a.append(int(part[i]))
    video.append(a)

_zip = ''

def DivideAndConquer(N, y, x):
    global _zip

    if N == 0:
        return

    subVideo = [col[x:x+N] for col in video[y:y+N]]

    # 모두 1일 경우 -> 1로 압축 가능
    if all(all(x) for x in subVideo):
        _zip += '1'
        return 
    if any(any(x) for x in subVideo) == False:
        _zip += '0'
        return

    _zip += '('

    DivideAndConquer(N//2, y, x)
    DivideAndConquer(N//2, y, x+N//2)
    DivideAndConquer(N//2, y+N//2, x)
    DivideAndConquer(N//2, y+N//2, x+N//2)

    _zip += ')'

DivideAndConquer(N, 0, 0)
print(_zip)