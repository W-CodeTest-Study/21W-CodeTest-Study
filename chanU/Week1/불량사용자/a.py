import copy

def cmp(x, y):
    for i in range(0, len(x)):
        if x[i] == '*' or y[i] == '*':
            continue
        if x[i] != y[i]:
            return False
    return True

s = list()
tmp = list()

def solution(user_id, banned_id):
    answer = 0
    
    if len(banned_id) == 0:
        if str(sorted(tmp)) not in s:
            s.append(str(sorted(tmp)))
        return
    
    for i in user_id:
        if len(i) == len(banned_id[0]) and cmp(i, banned_id[0]):
            tmpu_id = copy.deepcopy(user_id)
            tmp.append(i)
            tmpu_id.pop(user_id.index(i))
            tmpb_id = copy.deepcopy(banned_id)
            tmpb_id.pop(0)
            solution(tmpu_id, tmpb_id)
            if len(tmp) > 0:
                tmp.pop(-1)

    return len(s)
