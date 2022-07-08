n2 = [] # 입력을 저장하는 리스트
temp_list = [] # 연산을 위한 리스트

n = int(input())
for i in range(n):
    n2 = list(map(int, input().split())) # list, split을 사용해 연속적인 입력을 처리한다.
    avg = sum(n2[1:])/(len(n2)-1)
    above_avg_cnt = 0
    # filter(함수, 리스트) 람다 함수의 조건에 맞는 항목만 리스트에 남긴다.
    temp_list = list(filter(lambda x: x > avg, n2[1:]))
    above_avg_rate = len(temp_list)/(len(n2)-1) * 100 # 평균 이상 점수 비율 계산.
    print(f'{above_avg_rate:.3f}%') # 출력


