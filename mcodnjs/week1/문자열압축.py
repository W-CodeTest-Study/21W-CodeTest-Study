def func(string_list):
    num = 0
    remain = []
    temp = 0 # 10 넘는지 확인하는 용도
    for idx, data in enumerate(string_list):
        if idx == len(string_list)-1:
            remain.append(data)
            break
        if data == string_list[idx+1]:
            if temp == 0 or temp == 8: 
                num += 1
            temp += 1
        else: 
            temp = 0
            remain.append(data)
    return num + len(''.join(remain))
    
def solution(s):
    answer = 0
    length = []
    for i in range(1,len(s)+1): # 자르는 단위
        j = 0
        string_list = []
        while j < len(s): # 문자열 길이
            string_list.append(s[j: j+i])
            j = j + i
        length.append(func(string_list))
        
    answer = min(length)
    return answer
