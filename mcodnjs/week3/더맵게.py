import heapq
heap = []

def solution(scoville, K):
    answer = 0
    for sco in scoville:
        heapq.heappush(heap, sco)
    heapq.heapify(heap)
    
    while True:
        
        if not heap:    return -1
        if heap[0] > K:     return answer
        if len(heap) < 2:   return -1
        
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        mix = first + 2*second
        
        heapq.heappush(heap, mix)
        answer += 1
        
    return answer