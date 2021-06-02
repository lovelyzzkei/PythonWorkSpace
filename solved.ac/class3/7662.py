import sys; read = sys.stdin.readline
import heapq

result = []
for _ in range(int(read())):
    min_heap = []; max_heap = []
    visited = [False] * 1_001_001   # 해당 숫자가 제거되었는지 확인을 위한 구분자

    for i in range(int(read())):
        s = read().split()
        if s[0] == 'I':
            heapq.heappush(min_heap, (int(s[1]), i))
            heapq.heappush(max_heap, (-int(s[1]), i))
            visited[i] = True

        # 최댓값 삭제
        elif s[1] == '1':
            # 최대 힙의 최댓값 노드가 최소 힙에서 제거된 노드라면 최대 힙에서도 제거
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            
            # 원소가 있을 경우에만 제거
            if max_heap:
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)
        
        # 최솟값 삭제
        else:
            # 최소 힙의 최솟값 노드가 최대 힙에서 제거된 노드라면 최소 힙에서도 제거
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)

            # 원소가 있을 경우에만 제거
            if min_heap:
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)
            
    # 혹여나 동기화가 안된 노드들이 있다면 제거
    while max_heap and not visited[max_heap[0][1]]: heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]: heapq.heappop(min_heap)

    result.append(f'{-max_heap[0][0]} {min_heap[0][0]}' if max_heap and min_heap else 'EMPTY')

print('\n'.join(result))

