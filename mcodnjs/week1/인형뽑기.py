def solution(board, moves):
    answer = 0
    stack = []
    
    for i in moves:
        if not len(stack) <= 1 and stack[len(stack)-1] == stack[len(stack)-2]:
            stack.pop()
            stack.pop()
            answer += 2
            
        for j in range(len(board)):
            if not board[j][i-1] == 0:
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
            
    return answer
