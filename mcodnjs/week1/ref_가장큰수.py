def solution(numbers):
    answer = ''
    string = list(map(str, numbers))
    string.sort(key = lambda x : x*3, reverse = True)
    answer = str(int(''.join(string)))
    return answer
