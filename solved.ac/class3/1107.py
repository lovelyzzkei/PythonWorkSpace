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

# 수 생성 함수
nums = []
num = 0
def create_num(length):
    global num
    if length == 0:
        nums.append(num)
        return

    for a1 in REMOTE:
        num += a1 * pow(10, length - 1)
        create_num(length - 1)
        num -= a1 * pow(10, length - 1)

# 순차 탐색 함수
def search():
    diff = 9999999999
    for num in nums:
        if abs(num - N) < diff:
            diff = abs(num - N)
            ans = num
    return ans


# 리모컨에서 사용할 수 있는 숫자들로 1~6자리의 숫자를 만든 뒤
# 그 숫자들에서 찾으려고 하는 숫자와 가장 가까운 숫자를 찾는다
# 이때 찾을 때는 수가 많지 않으므로 순차탐색 사용


if _ == 0:
    ans.append(len(str(N)))
elif _ != 10:
    # 리모컨에서 사용할 수 있는 숫자들로 만든 수들
    for i in range(1, 7):
        create_num(i)

    nearest_num = search()
    ans.append(len(str(nearest_num)) + abs(nearest_num - N))

print(min(ans))