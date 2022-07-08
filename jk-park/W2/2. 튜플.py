def solution(s):
    # s = input()  # 입력
    # 괄호 짝이 5개라면, 4개의 집합이 포함되어 있다. -> 튜플의 원소의 개수가 4개.

    l_bracket_cnt = s.count('{')
    r_bracket_cnt = s.count('}')

    bracket_place_list = []  # 괄호가 있는 부분의 인덱스를 저장. 0과 짝수 index는 왼쪽 괄호, 홀수는 오른쪽 괄호
    bracket_split_list = []  # 괄호를 기준으로 나눈 사이에 들어간 숫자 리스트를 담는 이차원리스트

    result_list = []

    for i in range(len(s)):
        if i == 0 or i == len(s) - 1:  # 첫 bracket과 마지막 bracket 추가x
            continue
        if s[i] == '{' or s[i] == '}':
            bracket_place_list.append(i)

    for i in range(len(bracket_place_list)):
        if i % 2 != 0:
            continue
        l = bracket_place_list[i]
        r = bracket_place_list[i + 1]
        temp_list = []  # 2차원 리스트를 위한 temp_list
        for j in range(l + 1, r):  # 괄호 사이를 도는 for문
            temp_list.append(s[j])
        temp_str = ''.join(temp_list)  # temp_list를 문자열로 변환
        bracket_split_list.append(list(map(int, temp_str.split(','))))  # 문자열을 콤마를 기준으로 리스트로 변환 ex) "123,23,3" -> [123, 23, 3]
    bracket_split_list.sort(key=len)  # 리스트의 길이를 key로 리스트 정렬

    for split_list in bracket_split_list:  # 결과 리스트 정리
        for i in split_list:
            if i not in result_list:
                result_list.append(i)

    return result_list

s="{{2},{2,1},{2,1,3},{2,1,3,4}}"

print(solution(s))


