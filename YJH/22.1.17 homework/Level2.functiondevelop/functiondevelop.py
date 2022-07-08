import math
def solution(progresses, speeds):
    day=[]
    answer=[]
    cnt=1   #배포되는 작업의 수
    for i in range(len(progresses)):
        day.append(math.ceil((100-int(progresses[i]))/int(speeds[i])))  #각각의 progresses들이 얼마나 걸릴지를 계산해서 day에 추가해준다.
    max=day[0]  #첫번째게 배포되어야 뒤에것들이 배포될 수 있기 때문에 첫번째 day를 max로 설정해준다.
    for i in range(1,len(day)): 
        if day[i]<=max: #max보다 해당 day가 작거나 같으면 같이 배포될 수 있는 것이기 때문에 cnt를 +1해준다.
            cnt+=1
        elif day[i]>max:    #max보다 해당 day가 크면 앞에 있는 친구들과 같이 배포 될 수 없다.
            answer.append(cnt)  
            max=day[i]
            cnt=1   #그래서 cnt를 answer에 추가해서 배포해버리고, cnt와 max를 다시 설정해준다. 
    answer.append(cnt)
    return answer