def solution(s):
    cnt=[]
    answer={}
    ranswer=[]
    s=s.replace('{','').replace('}','') #들어온 문자열의 괄호들을 다 없애준다
    s=s.split(',')  #남은 s에 있는 문자열을 ,를 기준으로 list로 바꿔준다.
    for i in range(len(s)): #s만큼 돌면서 숫자들만 새로운 배열인 cnt에 추가해준다.
        if s[i].isdigit():
            cnt.append(s[i])
    b=list(set(cnt))    #새로운 리스트의 중복을 제거해준다. 
    for i in range(len(b)): #만들어놓은 딕셔너리에 b의 인덱스들을 key로 저장하고 b의 인덱스가 cnt에 담긴 숫자만큼 value로 정해준다.
        answer[b[i]]=cnt.count(b[i])
    answer=sorted(answer.items(),key=lambda x:x[1],reverse=True)    #value값이 높을수록 많은 인덱스에 포함되어 있는 것이기 때문에 가장 앞에 있는 친구다. 이를 참고하여 람다로 딕셔너리를 정렬해준다.
    for i in range(len(answer)):
        ranswer.append(int(answer[i][0]))   #정렬해준 친구를 답에 추가해준다.
    return ranswer