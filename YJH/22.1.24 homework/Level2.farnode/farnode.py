from collections import deque
def solution(n, edge):
    edge.sort()
    cnt = deque()
    a = [[] for x in range(n+1)]
    v = [0]*(n+1)
    answer=0
    for i in edge:
        a[i[0]].append(i[1])
        a[i[1]].append(i[0])
    cnt.append(1)
    v[1]=1
    while cnt:
        c = cnt.popleft()
        for j in a[c]:
            if v[j]==0:
                cnt.append(j)
                v[j]=v[c]+1
    m = max(v)
    for k in v:
        if k == m:
            answer+=1
    return answer