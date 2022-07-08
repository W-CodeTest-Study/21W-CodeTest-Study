# 1~6번, 11번 Testcase 실패
# 구글링 코드 참고 -> ref_[].py
import math
def func(numbers, digit):
    
    max_digit = max(digit) # digit 중 가장 큰 수 
    max_index = digit.index(max_digit) # digit 중 가장 큰 수가 위치한 idx
    print("numbers, digit:", numbers, digit)
    store = numbers
    while digit.count(max_digit) > 1:
        max_digit = max(digit) # digit 중 가장 큰 수 
        max_index = digit.index(max_digit) # digit 중 가장 큰 수가 위치한 idx
        new_numbers = []
        new_digit = []
        new_store = []
        for idx, value in enumerate(store):
            if digit[idx] == max_digit:
                new_numbers.append(numbers[idx])
                num = len(str(value))
                num = math.pow(10, num-1)
                if value < 10:
                    new_digit.append(value)
                    new_store.append(value)
                else: 
                    temp = value-int(num)*digit[idx]
                    new_store.append(temp)
                    num = len(str(temp))
                    num = math.pow(10, num-1)
                    new_digit.append(int(temp/num))
        
        
        print("new_numbers:", new_numbers)
        print("new_store:", new_store)
        print("new_digit:", new_digit)
        digit = new_digit
        numbers = new_numbers
        store = new_store

        max_digit = max(digit)
        print("count:", digit.count(max_digit))
        max_index = digit.index(max_digit)
        # print("index:", max_index)
        if len(list(set(new_store))) == 1:
            if max(list(set(new_store))) == 0:
                return max_index, min(list(set(numbers)))
            return  max_index, numbers[max_index]
    return max_index, numbers[max_index]
    
def first(numbers): # 가장 큰 첫번째 자릿수를 가진 index와 value 리턴
    digit = []
    for idx, value in enumerate(numbers):
        num = len(str(value))
        num = math.pow(10, num-1)
        if not value == 0:
            digit.append(int(value/num))
        else:
            digit.append(value)  
    return func(numbers, digit)


def solution(numbers):
    print(numbers)
    answer = ''
    print("==========================================")
    while not len(numbers) < 1:
        print("Before list: ", numbers)
        index, value = first(numbers)
        print("deleted value: ", value)
        numbers.remove(value)
        print("After list: ", numbers)
        answer += str(value)
        print("==========================================")
    print("answer: ", answer)
    return answer

