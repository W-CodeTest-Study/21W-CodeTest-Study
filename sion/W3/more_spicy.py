import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            return answer
        min2 = heapq.heappop(scoville)
        new_food = min1 + min2 * 2
        heapq.heappush(scoville, new_food)
        answer += 1
    if scoville:
        if heapq.heappop(scoville) >= K:
            return answer
        answer = -1
    
    return answer
