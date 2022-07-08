a, b = list(map(int, input().split()))  # python3는 시간 초과가 나서 PyPy3로 채점받기
house = []
for i in range(a):
    house.append(int(input()))
house.sort()
start = 1
end = house[-1] - house[0]
answer = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    num = house[0]
    for i in range(1, a):
        if house[i] >= num + mid:
            cnt += 1
            num = house[i]

    if cnt >= b:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)
