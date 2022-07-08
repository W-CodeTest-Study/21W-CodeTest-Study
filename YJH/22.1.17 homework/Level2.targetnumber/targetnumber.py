def solution(numbers, target):
    answer = 0
    leaves=[0]
    for num in numbers:
        tmp=[]
        for parent in leaves:   #tmp 배열에 가능한 모든 경우의수를 넣어준다. 
            tmp.append(parent+num)  #+num이 되는 경우
            tmp.append(parent-num)  #-Num이 되는 경우를 다 넣어준다.
        leaves=tmp
    for i in range(len(leaves)):
        if target==leaves[i]:   #넣어준 배열이 target과 같다면 answer+=1
            answer+=1
    return answer
