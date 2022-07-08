def uv(p):
    open_p = 0
    close_p = 0

    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i + 1], p[i + 1:]
def check(u):
    a=[]
    if u[0]==')':
        return False
    else:
        for i in range(len(u)):
            if u[i]=='(':
                a.append(u[i])
            else:
                a.pop()
        if len(a)==0:
            return True
        else:
            return False
def solution(p):
    if not p:
        return ''
    u,v = uv(p)
    if check(u):
        answer=u+solution(v)
        return answer
    else:
        answer='('
        answer+=solution(v)
        answer+=')'
        u=u[1:]
        u=u[:-1]
        u=u.replace('(','0').replace(')','1')
        u=u.replace('0',')').replace('1','(')
        answer+=u
        return answer