def solution(s):
    s_list = s.split('},{')
    s_list[0] = s_list[0][2:] # '{{' 제거
    s_list[len(s_list)-1] = s_list[len(s_list)-1][:-2] # '}}' 제거
    
    s_list.sort(key=lambda x: x.count(','))
    
    # print(s_list)
    answer = []
    for i in range(len(s_list)):
        tmp_list = list(map(int, s_list[i].split(',')))
        for tmp in tmp_list:
            if tmp not in answer:
                answer.append(tmp)
    
    return answer
