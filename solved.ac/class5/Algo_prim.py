node_num = n
visited = {}
d = []

def get_min_node():
    for i in range(node_num):
        if not visited[i]:
            v = i
            break
    for i in range(node_num):
        if not visited[i] and d[i] < d[v]:
            v = i
    return v

def prim(start):
    d[start] = 0
    for i in range(node_num):
        node = get_min_node()
        visited[node] = True

        for j in range(node_num):
            if MAP[node][j] != INF:
                if not visited[j] and MAP[node][j] < d[j]:
                    d[j] = MAP[node][j]
                    