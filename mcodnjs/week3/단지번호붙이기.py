from collections import deque
array = []
N = int(input())

for i in range(N):
    string = list(input())
    array.append(string)

queue = deque()
answer = []

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        
        num = 0
        if array[i][j] == -1: continue
        if array[i][j]  == '0': continue
        if array[i][j]  == '1':
            array[i][j] = -1  # 방문한 곳은 -1로 표시
            queue.append((i,j))

        while queue:
            num += 1 # 큐에 한 집이 들어갈 때마다 num ++
            x, y = queue.popleft()

            for k in range(4):

                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:  continue
                if array[nx][ny] == -1: continue
                if array[nx][ny] == '0': continue
                if array[nx][ny] == '1':
                    array[nx][ny] = -1
                    queue.append((nx, ny))
        answer.append(num)

answer.sort() # 오름차수 정렬
print(len(answer))
for ans in answer:  print(ans)
