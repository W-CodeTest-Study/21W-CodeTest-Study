import sys

a,b = list(map(int, input().split()))
read = list(map(int, sys.stdin.readline().split()))
start , end = 1, max(read)
while(start <= end):
    sum = 0
    mid = (start + end)//2
    for i in read:
        cnt = i - mid
        if cnt > 0:
            sum += cnt
    if sum==b:
        print(mid)
        break
    elif sum >b:
        start = mid +1
    elif sum <b:
        end = mid -1