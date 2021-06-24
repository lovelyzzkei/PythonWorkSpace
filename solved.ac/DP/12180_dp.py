import sys; read = sys.stdin.readline
t = int(read())
arr = [[0 for i in range(11)] for j in range(11)]
arr[0][1] = 1
for i in range(1, 11):  # 네모 칸의 크기를 늘려가면서 가능한 경로의 수를 저장
    for j in range(1, 11):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]
for _ in range(t):
    r, c = map(int, read().split())
    print(f"Case #{_+1}: {arr[r][c]}")