from collections import deque

adj_list = {0:[2,3], 1:[3,4], 2:[3,5], 3:[5], 4:[5], 5: []}

def topological_sort(adj_list):
    q = deque([])
    in_degree = [0] * len(adj_list)
    answer = []

    # in-degree 배열 작성
    for i in range(len(adj_list)):
        for j in range(len(adj_list)):
            temp = adj_list[j]
            for k in range(len(temp)):
                if temp[k] == i:
                    in_degree[i] += 1

    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            q.append(i)
    
    while q:
        node = q.popleft()
        answer.append(node)

        for i in range(len(adj_list[node])):
            idx = adj_list[node][i]
            in_degree[idx] -= 1
            if in_degree[idx] == 0:
                q.append(idx)
    
    print(answer)

topological_sort(adj_list)