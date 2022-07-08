def inverse(u):
    u = list(u)
    
    for i in range(0, len(u)):
        if u[i] == '(':
            u[i] = ')'
        else:
            u[i] = '('
    return ''.join(u)

def isValid(u):
    n = 0
    for i in u:
        if i == '(':
            n += 1
        else:
            n -= 1
        
        if n < 0:
            return False
    return True

def process(w):
    n = 0
    
    if len(w) == 0 or isValid(w):
        return w
    
    for i in range(0, len(w)):
        if w[i] == '(':
            n += 1
        else:
            n -= 1
        
        if n == 0:
            u = w[0:i + 1]
            v = w[i + 1:]
            break
    
    if isValid(u):
        return u + process(v)
    else:
        s = '('
        s += process(v)
        s += ')'
        s += inverse(u[1:-1])
        return s
        
            

def solution(p):
    answer = process(p)
    return answer
