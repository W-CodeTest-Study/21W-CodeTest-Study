def func(m, n, board, cnt):

    for i in range(0,m): # string -> list
        board[i] = list(board[i])

    x, y = [], []
    for i in range(0,m-1):
        for j in range(0,n-1):
            target = board[i][j]
            if target == "1":   continue # 비어있는 칸 break 안됨
            if target == board[i][j+1] and target == board[i+1][j] and target == board[i+1][j+1]:
                # target == Right == Down == Right Down
                x.append(i)
                y.append(j)
    
    if len(x) == 0 and len(y) == 0: # 더이상 2x2 로 같은 칸이 없다면 종료 
        return board, cnt, False

    for i in range(len(x)): # 2x2 0으로 세팅
        board[x[i]][y[i]] = "0"
        board[x[i]][y[i]+1] = "0"
        board[x[i]+1][y[i]] = "0"
        board[x[i]+1][y[i]+1] = "0"
        
    for i in range(m): # 0 개수 
        cnt += board[i].count("0")

    # 행, 열 transpose algorithm
    board.reverse() 
    horizontal, vertical = [], []
    for j in range(n):
        vertical = []
        for i in range(m):
            vertical.append(board[i][j])
        horizontal.append(vertical)

    # list에서 0 삭제하고 1(비어있음)로 채움 -> 실제 블록이 내려가는 형태로 구현
    for i in range(n): 
        while "0" in horizontal[i]: horizontal[i].remove("0")
        while len(horizontal[i]) < m: horizontal[i].append("1")

    # 행, 열 transpose algorithm
    result = []
    for i in range(m):
        vertical = []
        for j in range(n):
            vertical.append(horizontal[j][i])
        result.append(vertical)
    result.reverse()
    
    for i in range(0,m): # string -> list
        result[i] = ''.join(result[i])
    return result, cnt, True


def solution(m, n, board):
    answer = 0  
    # 아래, 오른쪽, 대각선 아래 판단   
    while True:
        board, answer, flag = func(m, n, board, answer) 
        if flag == False: # 더이상 2x2 로 같은 칸이 없다면 종료 
            break
    return answer


board=["CCBDE", "AAADE", "AAABF", "CCBBF"]
solution(4, 5, board)

# board=["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
# solution(6, 6, board)
# solution(7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"])