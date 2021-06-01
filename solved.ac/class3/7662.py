import sys
import heapq

T = int(sys.stdin.readline())
for _ in range(T):
    heap = []
    max_heap = []

    K = int(sys.stdin.readline())

    for __ in range(K):
        operation, input = sys.stdin.readline().split()

        if operation == 'I':
            heapq.heappush(heap, int(input))
            heapq.heappush(max_heap, -int(input))
    
        elif operation == 'D':
            # 리스트에 원소가 없을 경우 패스
            if len(heap) == 0:
                continue

            if input == '-1':
                min_num = heapq.heappop(heap)
                max_heap.remove(-min_num)
                heapq.heapify(max_heap)

            else:
                max_num = heapq.heappop(max_heap)
                heap.remove(-max_num)
                heapq.heapify(heap)

    if len(heap) == 0:
        print('EMPTY')
    else:       
        print(max(heap), min(heap))