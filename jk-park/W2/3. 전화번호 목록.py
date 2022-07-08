# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우 확인
# 전화번호 배열 -> phone_book
# 어떤 번호가 다른 번호의 접두어인 경우 false
# or true

def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] in phone_book[j][:len(phone_book[i])]:
                answer = False
                return answer
    return answer

phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))