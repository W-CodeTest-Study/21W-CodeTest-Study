def dfs(computers, node, visited):

    visited[node] = 1
    computer = computers[node]
    for i in range(len(computer)):
        if computer[i] == 1 and i != node and visited[i] == 0:
            visited[i] = 1
            dfs(computers, i, visited)

def solution(n, computers):

    visited = [0]*n
    answer = 0
    for node in range(n):
        if visited[node] == 0: 
            dfs(computers, node, visited)
            answer += 1
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
solution(n, computers)