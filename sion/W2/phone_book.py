def solution(phone_book):
    phone_book.sort()
    
    for index, phone in enumerate(phone_book):
        if index == len(phone_book)-1: break
        i = len(phone)
        if phone == phone_book[index+1][:i]:
            return False
        
    return True
