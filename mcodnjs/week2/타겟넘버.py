stack = [] # 트리 순회 확인용 스택 
temp = [] # 모든 결과값 리스트

def search(result, numbers, flag):
    if flag == "+":
        result += numbers[0]
    if flag == "-":
        result -= numbers[0]
    if not len(numbers)-1: 
        stack.append(numbers[0])
        temp.append(result)
        return result

    stack.append(numbers[0])
    stack.append("+")
    search(result, numbers[1:], "+")
    stack.append("-")
    search(result, numbers[1:], "-")
    return result

def func(temp, target): # 결과값 리스트에서 target과 같은 값만 카운트
    num = 0
    for t in temp:
        if t == target: num += 1
    return num

def solution(numbers, target):
    answer = 0
    search(0, numbers, "+")
    search(0, numbers, "-")
    answer = func(temp, target)
    return answer