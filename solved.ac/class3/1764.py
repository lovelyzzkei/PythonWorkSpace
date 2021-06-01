import sys

N, M = map(int, sys.stdin.readline().split())

a = sorted([sys.stdin.readline().strip() for _ in range(N)])
b = sorted([sys.stdin.readline().strip() for _ in range(M)])

# merge sort의 개념 활용
pointerA = 0
pointerB = 0
ans = []

while pointerA != N and pointerB != M:
    if a[pointerA] == b[pointerB]:
        ans.append(a[pointerA])
        pointerA += 1; pointerB += 1

    elif a[pointerA] < b[pointerB]:
        pointerA += 1
    else:
        pointerB += 1

if pointerA == N:
    for i in range(pointerB, M):
        if b[i] == a[pointerA - 1]:
            ans.append(b[i])

elif pointerB == M:
    for i in range(pointerA, N):
        if a[i] == b[pointerB - 1]:
            ans.append(a[i])

print(len(ans))
for name in ans:
    print(name)
