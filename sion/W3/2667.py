from collections import deque

n = int(input())
maps = [list(map(int, input())) for _ in range(n)]

def bfs(x, y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  count = 1

  queue = deque()
  queue.append((x, y))
  maps[x][y] = 2
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if maps[nx][ny] == 1:
        maps[nx][ny] = 2
        queue.append((nx, ny))
        count += 1
  return count

result = []
for i in range(n):
  for j in range(n):
    if maps[i][j] == 1:
      result.append(bfs(i, j))

print(len(result))
for r in sorted(result):
  print(r)
