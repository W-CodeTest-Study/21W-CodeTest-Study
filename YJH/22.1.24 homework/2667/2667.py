import sys

def dfs(x,y,m):
    if x<=-1 or x>=n or y<=-1 or y>=n:  #범위를 벗어나면 무조건 종료시킨다
        return False
    else:
        if a[x][y]==1 and gone[x][y]==0:    #a[x][y]가 1, 사람이 사는 곳이고 gone[x][y]가 0, 아직 방문하지 않은 곳이라면
            gone[x][y]=1    #방문처리를 해준 뒤
            a[x][y]=m       #넘어온 m을 사용해서 a리스트를 재설정 해준다.
            dfs(x,y+1,m)    #그리고 a[x][y]의 상하좌우에 대해서 dfs를 돌려주며 확인해준다. 
            dfs(x,y-1,m)
            dfs(x-1,y,m)
            dfs(x+1,y,m)
n = int(sys.stdin.readline())
a=[[]for i in range(n)]
cnt=1
answer={}
for i in range(n):
    read = sys.stdin.readline().split()
    for j in range(n):
        a[i].append(int(read[0][j]))
gone = [[0 for i in range(n)]for i in range(n)]
for i in range(n):
    for j in range(n):
        dfs(i,j,cnt)
        cnt+=1
for i in range(n):
    for j in range(n):
        if a[i][j] !=0:
            if a[i][j] not in answer:
                answer[a[i][j]]=1
            else:
                answer[a[i][j]]+=1
answer = sorted(answer.items(), key = lambda x:x[1])
print(len(answer))
for i in range(len(answer)):
    print(answer[i][1])