def solution(m, n, board):
    count = 0
    for k in range(m*n):
        delcnt=[]   #터질 좌표의 기준점 추가해주는 array
        for i in range(len(board)):
            board[i] = list(board[i])
        for i in range(len(board)-1):
            for j in range(len(board[0])-1):
                cnt = board[i][j]
                if cnt == board[i][j+1] and cnt == board[i+1][j] and cnt == board[i+1][j+1]:   #옆,밑, 대각선이 같으면
                    delcnt.append([i,j])    #해당 좌표를 터질 좌표의 기준점 추가
        for j in range(len(delcnt)):    #기준좌표 중심으로 옆,밑,대각선 모두 0으로 초기화
            x = int(delcnt[j][0])
            y = int(delcnt[j][1])
            board[x][y] = 0
            board[x][y+1] = 0
            board[x+1][y] = 0
            board[x+1][y+1] = 0
        for c in range(7): #내려주는 경우의 수를 각각의 경우에 맞게 해줘야 하지만 30*30에서 터질수 있는 최대 횟수는 7번(7*4 =28) 그래서 7번 돌아준다. 
            for i in range(len(board)): 
                for j in range(len(board[0])):  #board가0일 경우 내려준다. 바로 위를 내려준다. 
                    if board[i][j]==0 and i!=0:
                        board[i][j] = board[i-1][j]
                        board[i-1][j] = 0
    for p in range(len(board)): #0의 갯수 파악
        for q in range(len(board[0])):
            if board[p][q] == 0:
                count+=1
    return count