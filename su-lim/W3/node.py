from collections import deque, Counter

def get_node_list(n, edge):
    
    graph = [[] for i in range(n+1)]

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    return graph

def solution(n, edge):
    answer = 0
    queue = deque([1])
    visited = []
    shortest = [0]*(n+1) #1로 부터의 최단 거리 저장 리스트, 0과 1 인덱스는 쓰이지 않음

    # step1. 노드의 정보를 담은 2차원 배열 구현 (행-노드 인덱스)(열-노드에 연결된 다른 노드들(순서X))
    graph = get_node_list(n, edge)

    distance = 0
    # step2. 
    while(queue):
        now = queue.popleft()
        if now not in visited:
            # print(now)
            visited.append(now)
            adj = graph[now]
            for node in adj:
                if not shortest[node] and node != 1:
                    shortest[node] = shortest[now] + 1
                    queue += node

    answer = shortest.count(max(shortest))

    return answer