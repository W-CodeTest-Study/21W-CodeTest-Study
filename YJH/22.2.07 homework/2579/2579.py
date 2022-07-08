n = int(input())
floor = []
dp = [0]*301
for i in range(n):
    floor.append(int(input()))
if n==1:
    print(floor[0])
elif n==2:
    print(floor[0] + floor[1])
else:
    dp[0] = floor[0]
    dp[1] = floor[0] + floor[1]
    dp[2] = max(floor[0] + floor[2], floor[1] + floor[2])
    for i in range(3,n):
        dp[i] = max(dp[i-3]+floor[i-1]+floor[i], dp[i-2] + floor[i])
    print(dp[n-1])