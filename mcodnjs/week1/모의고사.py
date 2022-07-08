def solution(answers):
    answer = []
    people = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    correct = [0, 0, 0] # 수포자 1,2,3 맞은 개수
    
    for i in range(len(answers)):
        person = 1
        while person <= 3:
            if answers[i] == people[person][i% len(people[person])]:
                correct[person-1] += 1
            person += 1

    for i in range(3):
        if max(correct) == correct[i]:
            answer.append(i+1)
    return answer
