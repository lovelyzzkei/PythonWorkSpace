'''
세그먼트 트리: 여러 개의 데이터가 연속적으로 존재할 때 특정한 범위의 데이터의 합을 구하는 방법
완전 탐색으로 O(N)이 걸리는 부분 합을 O(logN)으로 줄이는 방법
'''

a = [2, 1, 4, 5, 1, 3, 3]
seg_tree = [0] * (len(a)*4)

# 트리 만들기 -> 분할 정복으로 구현
# start: 시작 idx, end: 끝 idx, node: 트리에 저장되는 idx
def init(start, end, node):
    if start == end:
        seg_tree[node] = a[start]
        return seg_tree[node]
    mid = (start + end) // 2
    seg_tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return seg_tree[node]

# 구간 합을 구하는 함수
# left, right: 구간 합을 구하고자 하는 범위
def sum(start, end, node, left, right):
    # 범위 밖에 있는 경우
    if left > end or right < start:
        return 0
    # 범위 안에 있는 경우
    if left <= start and end <= right:
        return seg_tree[node]
    mid = (start + end) // 2
    return sum(start, mid, node*2, left, right) + sum(mid+1, end, node*2+1, left, right)


print(init(0, len(a)-1, 1))
print(sum(0, len(a)-1, 1, 0, 7))
print(seg_tree)








