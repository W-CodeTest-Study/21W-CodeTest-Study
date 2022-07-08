import heapq

def solution(jobs):
    # 해당 시간에 처리할 수 있는 작업이 여러 개인 경우 종료시점이 빠른 것부터 우선순위 (이 알고리즘 생각해내는데 개오래걸렸음ㅠ)
    
    answer = 0
    work_length = len(jobs) # 총 들어온 작업 개수
    heapq.heapify(jobs) # 리스트 -> heap
    current = 0 # 현재 시간
    work = 0 # 수행한 작업 개수
    time = [] # 총 소요시간 = 대기시간(작업을 시작한 시점 - 작업이 요청되는 시점) + 작업시간

    while work < work_length:
        heap = []
        for job in jobs:
            if job[0] <= current:
                heapq.heappush(heap, (current + job[1], job))

        if heap: # heap이 비어있지 않으면
            pop = heapq.heappop(heap) # heap에서 삭제
            jobs.remove(pop[1]) # jobs에서 해당 작업 삭제
            
            wait_time = current - pop[1][0]
            work_time = pop[1][1]
            time.append(wait_time + work_time)
            
            work += 1
            current += pop[1][1]

        else:   current = jobs[0][0]

    answer = sum(time, 0.0)/len(time)
    return int(answer)