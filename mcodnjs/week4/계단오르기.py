'''
    < 알고리즘 >
        scores[1] - 앞에서 1칸 움직인 경우: 
            건너뛰거나 -> scores[0]
            1칸 더 움직여서 2칸 연속으로 움직임 -> scores[2]

        scores[2] - 앞에서 2칸 연속으로 움직인 경우:
            무조건 건너뛰기 -> scores[0]

        scores[0] -  앞에서 건너뛴 경우: 
            무조건 1칸 움직이기 -> scores[1]
'''

stairs = []
num = int(input())
for i in range(num):
    stairs.append(int(input()))

scores = [0]*3
temp = [0]*3 # 저장용 템프
scores[1] = stairs[0]

for stair in stairs[1:]:
    
    temp[1] = scores[0]+stair
    temp[2] = scores[1]+stair
    temp[0] = max(scores[1], scores[2])
    scores = temp.copy()

print(max(scores[1], scores[2]))