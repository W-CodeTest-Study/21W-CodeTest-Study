def solution(phone_book):
    phone_book.sort()   #들어온 번호들을 정렬해준다.
    a=0
    for i in range(len(phone_book)-1):  #리스트의 마지막 인덱스는 비교 당하기만 하면 되기 때문에 범위를 len(phone_book)-1 로 해준다.
        a=len(phone_book[i])    
        if phone_book[i]==phone_book[i+1][:a]: #바로 뒤에 있는 인덱스를 앞에 있는 인덱스의 길이만큼 슬라이싱해서 만약 같다면 접두사가 같은것이므로 false를 return 해준다.
            return False
    return True #무난하게 for문을 빠져나오면 True를 리턴해준다. 