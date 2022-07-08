# 괄호가 개수는 맞지만 짝이 맞지 않은 형태로 작성되어 발생하는 오류 확인.
# 소스코드의 모든 괄호를 뽑아서 올바른 순서로 배치

def make_u(input_str): # 문자열 분리
    l_br = 0
    r_br = 0
    for i in range(len(input_str)):
        if input_str[i] == '(':
            l_br += 1
        elif input_str[i] == ')':
            r_br += 1
        if l_br == r_br:
            u_point = i
            return input_str[:u_point+1], input_str[u_point+1:]

def right_bracket_check(u): # 올바른 괄호인지 확인
    bracket_stack = []
    for i in range(len(u)):
        if u[i] == '(':
            bracket_stack.append(u[i])
        else:
            if not bracket_stack:
                return False
            else:
                bracket_stack.pop()
    return True


def solution(p):
    answer = ''

    if not p:
        return ""

    u, v = make_u(p)
    print(u, v)
    if right_bracket_check(u):
        print("통과 u", u)
        return u + solution(v)

    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for i in u[1:len(u)-1]: # 앞뒤 괄호 제거
            if p == '(':
                answer+=')'
            else:
                answer += '('

        return answer

p = "()))((()"
print(solution(p))