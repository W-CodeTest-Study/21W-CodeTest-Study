def solution(user_id, banned_id):
    cnt = [[]]
    answer=[]
    for j in range(len(banned_id)):
        new=[]
        for i in range(len(user_id)):
            if len(user_id[i])==len(banned_id[j]):  #1차적으로 user와 ban의 id가 같으면 True, 아니면 False
                cnt1 = True #문자열이 같은지 다른지 check할 기준
                for p in range(len(banned_id[j])): 
                    if banned_id[j][p]=='*':    #*이 나오면 그냥 pass
                        continue
                    elif banned_id[j][p]==user_id[i][p]: #같아도 Pass
                        continue
                    else:   #문자열이 다를경우 False 변환
                        cnt1 = False
                        break
                if cnt1 == True:    #같으면
                    for c in cnt:   #cnt를 기준으로 for문 순회
                        if user_id[i] not in c: #만약 cnt의 인덱스 안에 해당 user_id가 없다면
                            new.append(c+[user_id[i]])  #앞의 것도 추가해서 새로운 리스트에 추가해준다.
            else:
                continue
        cnt = new   #여기서 새로운 리스트를 cnt로 옮겨준다음, new리스트는 다음 인덱스 비교를 위해 초기화
    for c in cnt:
        if set(c) not in answer:    #set(c)로 중복 제거
            answer.append(set(c))
    return len(answer)