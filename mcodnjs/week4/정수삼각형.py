def solution(triangle):

    for tri in reversed(triangle[:len(triangle)-1]):
        temp = []
        pop = triangle.pop() # 삼각형 맨 아랫줄 
        for j in range(len(pop)-1):
            temp.append( tri[j] + max(pop[j], pop[j+1]) ) # 왼쪽 오른쪽 중에 큰 거를 더함
        triangle.pop()
        triangle.append(temp)
    return triangle[0][0]

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)