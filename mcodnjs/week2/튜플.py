def solution(s):
    answer = []
    s = s[2:len(s)-2] # input 문자열 앞뒤 {{}} 자르기
    s = s.split("},{")
    s.sort(key=len) # list 요소 길이 단위로 정렬

    for element in s: # 집합 안에 있는 원소 (type=문자열)
        numbers = list(map(int, element.split(","))) # ,로 나눠주고 int로 바꿔줌
        for num in numbers:
            if num not in answer:
                answer.append(num)
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s= "{{1,2,3},{2,1},{1,2,4,3},{2}}"
# s= "{{20,111},{111}}"
solution(s)

