from math import floor

def compresser(s, num):
    l = floor(len(s) / num);
    n = 0
    c = ''
    
    part = s[0 : num]
    for i in range(0, l):
        if s[i * num : (i + 1) * num] == part:
            n += 1
        else:
            if n > 1:
                c += f'{n}'+part
            else:
                c += part
            part = s[i * num : (i + 1) * num]
            #print(part)
            n = 1

    if n > 1:
            c += f'{n}'+part
    else:
            c += part
            
    return c + s[(i + 1) * num: ]

def solution(s):
    answer = 1000
    for i in range(1, len(s) + 1):
        n = len(compresser(s, i))
        if answer > n:
            answer = n
    return answer
