def solution(s):
    answer = []

    s = s[1:]
    s = s[:-1]

    elemDict = {}

    for i in s:
        start = s.find('{')
        end = s.find('}') + 1
        tmp = s[start + 1 : end - 1]
        elemList = tmp.split(',')
        for j in elemList:
            if j in elemDict:
                elemDict[j] = elemDict[j] + 1
            else:
                elemDict[j] = 1
        s = s[end:]
            
        if len(s) < 1:
            break
    
    sorted_dict = sorted(elemDict.items(), key = lambda item: item[1], reverse = True)
    for i in sorted_dict:
        answer.append(int(i[0]))

    return answer
