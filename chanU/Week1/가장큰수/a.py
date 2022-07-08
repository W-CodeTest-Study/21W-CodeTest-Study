from functools import cmp_to_key

def cmp(a, b):
    x = int(f"{a}{b}")
    y = int(f"{b}{a}")
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

def solution(numbers):
    n = list(map(str, numbers))
    n = sorted(n, key=cmp_to_key(cmp),reverse=True)
    answer = str(int(''.join(n)))
    return answer
