from collections import deque

def check_right(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            if stack[-1] == '(':
                stack.pop()
    if stack:
        return False
    return True

def convert_to_right(w):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열 반환
    if not w:
        return '', w
    else:
        w = deque(w)
        nr_open, nr_close = 0, 0
        stack = []
        for i in list(w):
            if i == '(':
                stack.append(w.popleft())
                nr_open += 1
            elif i == ')':
                stack.append(w.popleft())
                nr_close += 1
            if nr_open == nr_close and nr_open != 0:
                break
        # 2. u, v로 분리하기
        u = ''.join(stack)
        v = ''.join(w)
        
        # 3. u가 "올바른 괄호 문자열"이라면 convert_to_right(v) 수행
        if check_right(u):
            return (u + convert_to_right(v)[0]), '' # 3-1. 결과를 u에 이어 붙인 후 반환
        # 4. u가 "올바른 괄호 문자열"이 아니라면
        else:
            tmp = '(' + convert_to_right(v)[0] + ')'
            u_list = list(u)
            new_u_list = []
            for i in range(len(u_list)):
                if i == 0 or i == len(u_list)-1: continue
                if u_list[i] == '(':
                    new_u_list.append(')')
                elif u_list[i] == ')':
                    new_u_list.append('(')
            return tmp + ''.join(new_u_list), ''
            
        return u, v
    
def solution(p):
    if (check_right(p)): return p
    else:
        u, v = convert_to_right(p)          
            
    return u
