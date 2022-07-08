from math import ceil

def solution(progresses, speeds):
    answer = []
    tmp = []
    tmpN = 0
    maxIdx = 0
    for i in range(0, len(progresses)):
        tmp.append(ceil((100 - progresses[i]) / speeds[i]))
        
    print(tmp)
        
    for i in range(0, len(tmp)):
        if tmp[i] > tmp[maxIdx]:
            maxIdx = i
            answer.append(tmpN)
            tmpN = 0
        tmpN += 1
    
    answer.append(tmpN)
    
    return answer
