def solution(progresses, speeds):
    result = [0]*100
    answer = []

    num = 0
    while len(progresses):
        for idx, speed in enumerate(speeds):
            progresses[idx] += speed

        while len(progresses):
            if progresses[0] >= 100 :
                del progresses[0]
                del speeds[0]
                result[num] += 1
            else: 
                num += 1
                break

    for value in result: # result 리스트에서 공백 제거
        if value != 0:  answer.append(value)
    print(answer)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
solution(progresses, speeds)

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
solution(progresses, speeds)