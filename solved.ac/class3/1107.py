import sys

REMOTE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

N = int(sys.stdin.readline())
_ = int(sys.stdin.readline())
if _ == 0:
    M = []
else:
    M = list(map(int, sys.stdin.readline().strip().split()))

# 고장난 버튼 제거
REMOTE = [x for x in REMOTE if x not in M]

ans = []
# +,-를 눌러서 가는 경우
ans.append(abs(N-100))

# 근접한 채널(동일한 채널)로 이동하여 +,-를 누르는 경우
cnt = 0
channel = ''
N = str(N)
for i in range(len(N)):
    findNum = int(N[i])
    if N[i] in REMOTE:
        channel.join(str(findNum))
    else:

        # 리모컨 버튼 중에서 현재 자리수와 가장 가까운 수 선택
        # 근접한 수가 
        diff = 9999999
        x = 0
        for j in REMOTE:
            if findNum < j:
                findNum += 10
            if abs(findNum - j) < diff:
                diff = abs(findNum - j)
                x = j

        channel += str(x)

print(channel, N)

ans.append(len(channel) + abs(int(channel) - int(N)))
print(min(ans))