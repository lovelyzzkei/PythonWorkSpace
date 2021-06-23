import sys; read = sys.stdin.readline

n, k = map(int, read().split())

# 물건의 정보 받기
# items = [0] + [list(map(int, read().split())) for _ in range(n)]
# dp = [[0 for _ in range(k+1)] for _ in range(n+1)]  # 가능 무게 X 물건의 개수 크기의 배열

# for num_item in range(1, n+1): # 물건을 한개씩 늘려가면서
#     for weight in range(1, k+1):    # 1~k까지 각 배낭의 무게마다 담을 수 있는 물건의 가치의 최댓값을 저장
#         if items[num_item][0] > weight:  # 지금 물건의 무게가 현재 배낭에 담을 수 있는 무게보다 크면
#             dp[num_item][weight] = dp[num_item-1][weight]   # 현재 배낭에 담을 수 있는 최대 무게는 이 물건을 담기 이전에 이 배낭에 담을 수 있는 최대 무게와 동일
#         else:   # 그렇지 않다면
#             # 현재 배낭에 담을 수 있는 최대 무게는
#             # 이 물건을 담기 이전에 이 배낭에 담을 수 있는 최대 무게와
#             # 이 물건의 무게만큼을 뺀 배낭에 담을 수 있는 최대 무게에 지금 물건의 무게를 더한 값 중 최댓값
#             dp[num_item][weight] = max(dp[num_item-1][weight], \
#                 dp[num_item-1][weight-items[num_item][0]] + items[num_item][1])

# print(max(max(x) for x in dp))

dp = [0] * (k+1)
for _ in range(n):
    w, v = map(int, read().split())

    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)

print(dp[k])