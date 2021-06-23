import sys; read = sys.stdin.readline
import heapq
INF = int(1e7)

n, k = map(int, read().split())

def dijkstra(start, end):
    d = [INF] * 100001
    d[start] = 0
    q = []
    count = 0       # 가장 빠른 시간으로 동생을 찾는 방법의 수를 저장하는 변수
    ans = 0        # 동생을 찾는 가장 빠른 시간을 저장하는 변수
    isMinTime = False
    heapq.heappush(q, (0, start)) 

    while q:
        dist, now = heapq.heappop(q)
        if now == end:
            ans = dist
            count += 1
            isMinTime = True

        # 동생을 찾았을 때 우선순위 큐에 해당 시간으로 동생을 찾는 다른 방법의 수가 없으면 종료
        if isMinTime:   
            if dist > ans:
                return [ans, count]

        if d[now] < dist:   # 이미 해당 지점을 더 빨리 갈 수 있으면 pass
            continue
            
        cost = dist + 1
        if now-1 > -1 and cost <= d[now-1]:
            d[now-1] = cost
            heapq.heappush(q, (cost, now-1))

        if now+1 < 100001 and cost <= d[now+1]:
            d[now+1] = cost
            heapq.heappush(q, (cost, now+1))
        
        if now*2 < 100001 and cost <= d[now*2]:
            d[now*2] = cost
            heapq.heappush(q, (cost, now*2))

    return [ans, count]


print('\n'.join(str(x) for x in dijkstra(n, k)))