from collections import deque
import math

def solution(board):
    answer = 0
    n = len(board)
    costs = [[math.inf]*n for _ in range(n)]
    costs[0][0] = 0
    
    def bfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        queue = deque()
        queue.append((x, y, -1, 0)) # x, y, direction, cost
        while queue:
            x, y, dr, cost = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                tmp_cost = cost + 100 if i == dr else cost + 600
                if x == 0 and y == 0:
                    tmp_cost = 100
                if board[nx][ny] == 0:
                    board[nx][ny] = 2
                    queue.append((nx, ny, i, tmp_cost))
                elif board[nx][ny] == 2:
                    if tmp_cost < costs[nx][ny]:
                        costs[nx][ny] = tmp_cost
                        queue.append((nx, ny, i, tmp_cost))
        
    bfs(0, 0)
    # for i in range(n):
    #     print(costs[i])
        
    return costs[n-1][n-1]
