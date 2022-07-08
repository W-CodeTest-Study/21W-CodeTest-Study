def grab(board, move):
    N = len(board[0])
    for i in range(0, N):
        if board[i][move] != 0:
            t = board[i][move]
            board[i][move] = 0
            return t
    return 0

def solution(board, moves):
    baguni = []
    answer = 0
    
    for i in moves:
        item = grab(board, i - 1)
        if item != 0:
            if len(baguni) > 0 and item == baguni[-1]:
                baguni.pop()
                answer += 2
            else:
                baguni.append(item)
    
    return answer
