from collections import deque

def solution(n, edge):
    answer = 0
    visited = [-1 for _ in range(n+1)]
    adj = [[] for _ in range(n+1)]
    for e in edge:
        x = e[0]
        y = e[1]
        adj[x].append(y)
        adj[y].append(x)
    
    def bfs(start):
        cost = 1
        queue = deque()
        queue.append((start, cost))
        while queue:
            v, c = queue.popleft()
            if visited[v] == -1:
                visited[v] = c
                for i in adj[v]:
                    queue.append((i, c+1))
        
    bfs(1)
    for v in visited:
        if v == max(visited):
            answer += 1
            
    return answer
