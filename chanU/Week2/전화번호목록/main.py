def solution(phone_book):
    lenSet = set()
    for i in phone_book:
        lenSet.add(len(i))
    for i in lenSet:
        tmpSet = set()
        for j in phone_book:
            if j[0:i] not in tmpSet:
                tmpSet.add(j[0:i]) 
            elif j[0:i] in phone_book:
                return False

    return True
