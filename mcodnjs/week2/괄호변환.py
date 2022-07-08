# 올바른 -> 스택 -> is_stack
# 균형잡힌 -> 괄호 개수 같음 -> balance

def is_stack(p):
    stack = []
    for bracket in p:
        if bracket == "(":  stack.append(bracket)
        else:
            if len(stack) == 0: return False
            stack.pop()
    if len(stack) == 0: return True

def balance(p):
    bal_p = ""
    bal_num = 0
    for bracket in p:
        bal_p += bracket
        if bracket == "(":  bal_num += 1
        else:   bal_num -= 1
        if bal_num == 0:    break
    return bal_p

def solution(p):
    answer = ''
    if is_stack(p):  return p
    else:
        u = balance(p)
        v = p[len(u):]
        # print("u, v:", u, v)
        if is_stack(u):
            answer += u + solution(v)
        else:
            string = "(" + solution(v) + ")"
            temp = u[1:len(u)-1]
            temp = temp.replace("(", "0").replace(")", "(").replace("0", ")")
            return string + temp
    return answer

# p="(()())()"
# solution(p)
# p=")("
# solution(p)
p="()))((()"
print(solution(p))