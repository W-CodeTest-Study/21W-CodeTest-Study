from collections import deque

directions = [[0, 1, 'R'], [1, 0, 'D'], [0, -1, 'L'], [-1, 0, 'U']]

def solution(board):

    N = len(board)
    queue = deque()

    queue.append([0, 0, 0, '-'])
    cost = [[0 for _ in board] for _ in board] # N x N 0으로 초기화
    
    while(queue):
        cur_x, cur_y, cur_cost, cur_dir = queue.popleft()
        if cur_x == N-1 and cur_y == N-1:  continue
        
        for direction in directions:
            x = cur_x + direction[0]
            y = cur_y + direction[1]
            new_cost = cur_cost
            new_dir = direction[2]

            if x == 0 and y == 0:   continue
            if 0 <= x < N and 0 <= y < N and board[x][y] != 1: # x,y 좌표가 범위 내에 있고 벽이 아니면,
                if cur_dir == '-': new_cost += 1
                elif (cur_dir == 'R' or cur_dir == 'L') and (new_dir == 'R' or new_dir == 'L'): new_cost += 1
                elif (cur_dir == 'R' or cur_dir == 'L') and (new_dir == 'D' or new_dir == 'U'): new_cost += 6
                elif (cur_dir == 'D' or cur_dir == 'U') and (new_dir == 'D' or new_dir == 'U'): new_cost += 1
                elif (cur_dir == 'D' or cur_dir == 'U') and (new_dir == 'R' or new_dir == 'L'): new_cost += 6

                if not cost[x][y]:
                    cost[x][y] = new_cost
                    queue.append([x, y, new_cost, new_dir])
                
                if new_cost < cost[x][y]+4:
                    if new_cost < cost[x][y]:
                        cost[x][y] = new_cost
                    queue.append([x, y, new_cost, new_dir])

    return cost[N-1][N-1] * 100
