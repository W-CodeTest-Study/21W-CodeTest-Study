from collections import deque
# board =[[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
# board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]	
# board = [[0,0,0],[0,0,0],[0,0,0]]	
board = [[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt=[[99999]*len(board)for x in range(len(board))]
cnt[0][0] = 0
queue = deque()
queue.append((0,0,0,1))
queue.append((0,0,0,3))
while(queue):
    x,y,z,dir = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        tmp = z +100 if dir == i else z+600
        if 0<= nx < len(board) and 0 <= ny < len(board):
            if board[nx][ny]==0 and tmp<=cnt[nx][ny]:
                cnt[nx][ny] = tmp
                queue.append((nx,ny,tmp,i))
                print(queue)
print(cnt)
