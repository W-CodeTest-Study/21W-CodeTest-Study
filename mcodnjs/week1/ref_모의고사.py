'''
    enumerate 사용하기
    해당 문제의 경우에는 대상의 수가 3개이므로 딕셔너리 대신 3개의 리스트를 사용하면 더 빨리 풀고 코드가 간결해보일 듯
    people1 = [1,2,3,4,5]
    people2 = [2,1,2,3,2,4,2,5]
    people3 = [3,3,1,1,2,2,4,4,5,5]
'''
def solution(answers):
    answer = []
    people = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    correct = [0, 0, 0] # 수포자 1,2,3 맞은 개수
    
    for idx, value in enumerate(answers):
        if value == people[1][idx%len(people[1])]:
            correct[0] += 1
        if value == people[2][idx%len(people[2])]:
            correct[1] += 1
        if value == people[3][idx%len(people[3])]:
            correct[2] += 1

    for i in range(3):
        if max(correct) == correct[i]:
            answer.append(i+1)
    return answer

