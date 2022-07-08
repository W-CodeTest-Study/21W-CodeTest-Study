from collections import deque

def solution(n, computers):
    visited = [False for _ in range(n)]
    
    def bfs(index):
        queue = deque()
        queue.append(index)
        while queue:
            index = queue.popleft()
            if visited[index]:
                continue
            visited[index] = True
            for i in range(n):
                if computers[index][i] == 1:
                    queue.append(i)
    
    count = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            count += 1
    
    
    return count
