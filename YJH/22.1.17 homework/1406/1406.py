import sys
import collections
a = sys.stdin.readline()
n = int(sys.stdin.readline())
b = collections.deque(a)    #시간 효율성을 조금 더 간결하게 하기 위해서 deque를 쓴다.
b.pop() #stdin.readline()으로 받아서 맨 뒤에 \n이 리스트에 들어가므로 b.pop()을 해줬다.
answer = ''
c = collections.deque() #커서를 항상 맨 뒤에나 맨 앞에 하기 위해서 커서를 옮길 때마다 옮겨진 문자들을 새로운 덱인 c에 저장해줘야 한다.
for i in range(n):
    read = sys.stdin.readline()
    if read[0] == 'L':
        if len(b) != 0: 
            cnt = b.pop()   #커서가 왼쪽으로 갔기 때문에 맨 오른쪽을 pop해주고
            c.appendleft(cnt)#pop된 친구를 c에 넣어준다.
    elif read[0] == 'D':
        if len(c) != 0:
            cnt = c.popleft()   #L과 반대로 구현해준다.
            b.append(cnt)
    elif read[0] == 'B':
        if len(b) != 0:
            b.pop() #B이므로 단순 삭제
    elif read[0] == 'P':
        b.append(read[2])   #P이므로 커서 바로 뒤에 들어온 문자열인 read[2]를 append 해준다.
print(''.join(list(b)+list(c)))
