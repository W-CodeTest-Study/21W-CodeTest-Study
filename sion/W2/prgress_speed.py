import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
        
    while days:
        first_day = days[0]
        new_days = deque()
        count = 0
        is_continuous = True
        for day in days:
            tmp_day = day - first_day
            new_days.append(tmp_day)
            if tmp_day > 0:
                is_continuous = False
            elif is_continuous:
                count += 1
        answer.append(count)
        for _ in range(count):
            new_days.popleft()
        days = new_days
    
    return answer
