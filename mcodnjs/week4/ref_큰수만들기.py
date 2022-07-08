def solution(number, k):

    answer = ''
    N = len(number) # input 값 길이
    length = N-k # 구할 답 길이
    index = -1 # 현재 index

    while length > 0:    

        if length == N-index-1:
            answer += number[index+1:]
            break

        m = max(number[index+1: N-length+1]) # 이 과정에서 시간초과 
        # 999999인 경우는 max로 모든 리스트 길이만큼 검사할 필요 없음
        # 따라서 max 값 사용 대신 max 알고리즘 직접 구현 + 9인 경우 바로 answer에 추가
        index += number[index+1:N-length+1].index(m) + 1
        answer += m
        length -= 1
    return answer