# 기능개발
# 각 기능은 100%일 때만 서비스에 반영.
# 뒤에 있는 기능이 앞보다 먼저 100%가 된 경우, 앞의 기능이 배포될 때 함께 배포된다.
# 배포되어야하는 순서대로 작업의 진도가 적힌 정수배열 progresses,
# 작업 개발 속도가 적힌 정수 배열 speeds
# 각 배포마다 몇개의 기능이 배포되는지를 return

import math

def solution(progresses, speeds):
    answer = []
    clear = []  # 작업을 끝내는 데 소요되는 시간
    current_high = 0
    for i in range(len(progresses)):
        clear.append(math.ceil((100-progresses[i])/speeds[i]))  # ceil 함수를 사용해서, 소요일 계산
    for i in range(len(clear)):
        if i == 0: # 첫번째 기능에 대해 answer에 요소 생성
            answer.append(1)
        elif clear[current_high] >= clear[i]:
            answer[len(answer)-1] += 1
        else: # 이전 기능 배포 이후에 배포되는 항목에 대한 처리
            current_high = i
            answer.append(1)
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))
