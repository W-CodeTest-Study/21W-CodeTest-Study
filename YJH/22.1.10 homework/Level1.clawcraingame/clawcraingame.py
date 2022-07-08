def solution(board, moves):
    answer = 0
    a=[0]*1000
    y=0
    for i in range(0,len(moves)):
        for x in range(0,len(board)):
            if board[x][moves[i]-1]!=0:
                a.append(board[x][moves[i]-1])
                board[x][moves[i]-1]=0
                break
    a.reverse()
    while True:
        if a[y] == a[y+1] and a[y+1]!=0:
            answer+=2
            a.pop(y)
            a.pop(y)
            y-=2
        elif a[y+1]==0:
            break
        y+=1
    return answer