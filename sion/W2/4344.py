c = int(input())

answer = []
for _ in range(c):
    # 0번째는 개수, 1번째부터 점수
    score_list = list(map(int, input().split()))
    mean_val = (sum(score_list) - score_list[0]) // score_list[0]

    count = 0
    for i in range(1, len(score_list)):
        if score_list[i] > mean_val:
            count += 1
    
    # 문자열 formatting
    result = '{:.3f}%'.format((count / score_list[0]) * 100)
    answer.append(result)
  
[print(i) for i in answer]

