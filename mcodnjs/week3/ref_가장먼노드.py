'''
# 시간초과 줄이기

1) check 알고리즘 변경 (실제 시간초과 줄인 알고리즘)
    전) 방문한 노드를 리스트에 추가하는 형태로 사용 
        -> 노드가 check 리스트에 있는지 확인할 때, "if node in/not in check" 형식으로 검사했어야 했음
    후) 방문하지 않은 노드는 0, 방문한 노드를 1로 업데이트
        -> 노드를 방문했는지 확인할 때, "if check[node] == 1" 형식으로 검사할 수 있음.

2) edge 들 방문할 때 모든 edge를 탐색하는 것이 아니라 특정 노드와 인접한 edge들만 탐색 (+ 더 시간줄였다고 생각하는 알고리즘)
    전) for edge in edges
    후) for edge in temp[vtx]

3) 결론: in / not in 의 시간복잡도 : O(N)
'''

from collections import deque
def solution(n, edge):

    length = [-1]*n # 노드 1로부터의 길이
    check = [0]*n # 방문했는지 체크 
    depth = 0
    
    vtx = 1 # 시작노드
    length[0] = 0 # 노드1은 길이 0

    queue = deque() # BFS를 큐로 구현

     # 1: [[1,2], [1,3]] <- 해당 노드랑 인접한 엣지들을 딕셔너리 형태로
    temp = { i+1 : deque() for i in range(n) }
    for e in edge:
        temp[e[0]].append(e)
        temp[e[1]].append(e)

    while True:
        check[vtx-1] = 1   
         # 시간초과코드 - check.append(vtx)
        depth = length[vtx-1] + 1
        
        for e in temp[vtx]:

            if check[e[0]-1] == 1 and check[e[1]-1] == 1: continue  # [1,2] : 1,2 둘다 방문한 노드면 아래 코드 실행 ㄴ 
            # 시간초과코드 - if e[0] in check and e[1] in check: continue
            
            queue.append(e)

            # 현재 탐색하고 있 노드와 인접한 노드 찾기 ([1,2] <- 이런 형태이므로 1이 탐색하고 있는 노드라면 2를 찾아야함 즉, vtx가 아닌 노드 찾기)
            if e[0] == vtx: i = e[1] 
            else:   i = e[0]

            if length[i-1] == -1 or depth <= length[i-1]: # -1(방문한 적 없음)이거나 현재 거리가 depth보다 크면 업데이트
                length[i-1] = depth

        if not queue:   break # 무한루프 탈출
        while queue: # 큐가 비거나 방문 안한 노드가 나올 때까지 무한 pop
            pop = queue.popleft()  # 큐 왼쪽 끝부터 pop
            
            if check[pop[0]-1] == 0: # pop[0] 방문안한 노드
                # 시간초과코드 - if pop[0] not in check: 
                temp[pop[1]].remove(pop)
                vtx = pop[0] # 방문 안한 노드를 vtx로 만들어줌
                break 
                
            if check[pop[1]-1] == 0: # pop[1] 방문안한 노드
                # 시간초과코드 - if pop[1] not in check: 
                temp[pop[0]].remove(pop)
                vtx = pop[1] # 방문 안한 노드를 vtx로 만들어줌
                break

    return length.count(max(length)) 
    # 이걸로 인한 시간초과는 아니었지만 측정된 시간을 봤을 때 대폭 감소함
    # for node in length:
    #     if node == max(length):
    #         answer += 1