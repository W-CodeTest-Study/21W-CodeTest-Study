import sys
number = int(input())
answer = []
for i in range(number):
    av = 0
    count = 0
    cnt = sys.stdin.readline().split()
    for j in range(1, len(cnt)):    #첫 번째는 학생 수가 들어오므로 1부터 for문을 돌아준다.
        av += int(cnt[j])   #평균을 계속 더해주고
    av = av/int(cnt[0])     #학생 수가 있는 cnt[0]을 나눠준다.
    for k in range(1, len(cnt)):    #평균 넘는 학생 수를 구하기 위해서 한 번더 for문을 돌아준다.
        if int(cnt[k]) > int(av):   
            count += 1      #평균 넘을 때마다 count+1
    answer.append(round(count/int(cnt[0]), 5))  #소수 3자리 까지 구해줘야 하므로 rount함수를 사용해서 반올림 해준다.
for p in range(len(answer)):
    print('%.3f' % (answer[p]*100)+'%') #조건에 맞게 출력
