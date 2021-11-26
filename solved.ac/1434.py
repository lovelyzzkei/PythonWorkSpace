import sys; read = sys.stdin.readline
from collections import deque

n, m = map(int, read().split())
box = deque(list(map(int, read().split())))
book = deque(list(map(int, read().split())))

ans = 0
while len(box) != 0 and len(book) != 0:

    if book[0] <= box[0]:
        box[0] -= book.popleft()
        if box[0] == 0:
            box.popleft()
    else:
        ans += box.popleft()
        
ans += sum(box)
print(ans)