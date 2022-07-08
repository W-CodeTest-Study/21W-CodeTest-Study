import sys
from collections import deque
n = int(sys.stdin.readline())
time = []
answer = []
sub = []
for i in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))
    time.append((a, b))
time = sorted(time, key=lambda x: (x[1], x[0]))
# 가장 빨리 끝나는 순으로 정렬, 가장 빨리 끝나는 게 두개일 수도 있기 때문에 일이 빨리 끝나는 순 즉, x[0]으로 정렬
cnt = time[0][1]
num = 1
for i in range(1, n):
    if cnt <= time[i][0]:
        cnt = time[i][1]
        num += 1
print(num)
