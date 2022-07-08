def solution(s):
    answer = 1001
    strzip=[]
    real=[]
    cnt=1
    for i in range(len(s)//2):
        for j in range(0,len(s),i+1):
            strzip.append(s[j:j+i+1])
        for p in range(1,len(strzip)):
            if strzip[p-1]==strzip[p]:
                cnt+=1
                if p==len(strzip)-1:
                    real.append(cnt)
                    real.append(strzip[p])
                    cnt=1
            else:
                if p==len(strzip)-1:
                    real.append(strzip[p])
                if cnt>1:
                    real.append(cnt)
                real.append(strzip[p-1])
                cnt=1
        if answer > len("".join(map(str,real))):
            answer=len("".join(map(str,real)))
        real=[]
        strzip=[]
    return answer if len(s)!=1 else 1
