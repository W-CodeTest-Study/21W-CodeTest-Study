import sys
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

left = 1
right = max(trees)
# print("trees:", trees)

while left <= right:  
    
    take = 0
    mid = (left + right)//2

    total = [tree-mid if tree>mid else 0 for tree in trees]
    take = sum(total)
    # 위와 동일 알고리즘이지만, 아래는 시간초과 .. 
    # for tree in trees:
    #     if tree > mid:   take += tree - mid

    if take >= M:   left = mid + 1
    else:   right = mid - 1
print(right)