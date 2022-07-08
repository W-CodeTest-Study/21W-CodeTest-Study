def dfs(start,visited,cnt):
    visited[start] = True
    for i in cnt[start]:
        if visited[i] == False:
            dfs(i,visited,cnt)

def solution(n, computers):
    cnt = [[]for x in range(n)]
    visited = [False]*n
    ans=0
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                if i != j:
                    cnt[i].append(j)
                    cnt[j].append(i)
    for i in range(n):
        if visited[i]==False:
            dfs(i,visited,cnt)
            ans+=1
    return ans