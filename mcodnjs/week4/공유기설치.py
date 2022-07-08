import sys
N, C = map(int, sys.stdin.readline().split())
homes = []
for _ in range(N):
    homes.append(int(sys.stdin.readline()))
homes.sort()

min_distance = 1
max_distance = homes[-1]-homes[0]
result = 0

while min_distance <= max_distance:
    router = C
    first = homes[0]
    mid = (min_distance + max_distance)//2
    
    for i in range(1, len(homes)):
        if homes[i] - first >= mid:
            router -= 1
            first = homes[i]
    if router <= 1: # 더 많은 공유기를 설치할 수 있음 -> 간격늘리기
        min_distance = mid + 1
        result = mid

    elif router > 1: # C개만큼의 공유기를 설치할 수 없음 -> 간격좁히기
        max_distance = mid - 1
print(result)