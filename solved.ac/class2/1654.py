import sys

k, n = map(int, sys.stdin.readline().split())

# 랜선 길이 저장
LAN_wire = []
for i in range(k):
    LAN_wire.append(int(sys.stdin.readline()))

def cnt_wire(longest):
    if longest == 0:
        return n

    cnt = 0
    for wire in LAN_wire:
        cnt += (wire // longest)
    return cnt

# K개의 랜선 중 가장 짧은 것부터 1씩 빼면서 가장 최대가 되는 길이 확인
longest = max(LAN_wire)

# 중간 지점 구역 찾기
while True:
    if cnt_wire(longest) <= n and cnt_wire(longest // 2) >= n:
        start = longest // 2
        end = longest

        # 두 구간 사이에서 랜선의 개수가 최대가 될 수 있는 길이 탐색
        if start == 0:
            print(1)
            exit(0)

        while start + 1 < end:
            mid = (start + end) // 2
            if cnt_wire(mid) < n:
                end = mid
            else:
                start = mid

        print(start)
        exit(0)
    longest //= 2