# 한 줄로 된 간단한 에디터 구현
# 영어 소문자만 기록 가능, 600,000 글자까지 입력.
# 커서는 문장 맨 앞 or 문장 맨 뒤 or 문장 중간 임의의 장소.
# 5 길이의 문자열이면, a b c d e -> 커a커b커c커d커e커
# 6개의 경우의 수가 있다. N -> N+1 커서
# 명령어 ->
#   L: 커서 왼쪽 한칸. (맨 앞이면 무시)
#   D: 커서 오른쪽 한칸. (맨 뒤면 무시)
#   B: 커서 왼쪽에 있는 문자 삭제. (맨 앞이면 무시)
#       -> 왼쪽으로 이동한 것처럼 보이지만, 실제로는 커서의 오른족에 있던 문자는 그대로.
#   P $: $라는 문자를 커서 왼쪽에 추가

# 초기 문자열 주어짐.
# 그 이후 입력한 명령어 차례로 주어짐.

input_list = list(input())  # 문자열 리스트 변환
top = len(input_list)

for i in range(int(input())):
    command = list(input().split())
    if command[0] == "L":  # 왼쪽으로 커서 이동
        if cursor == 0:
            continue
        cursor -= 1
    elif command[0] == "D":  # 오른쪽 커서 이동
        if cursor == len(input_list):
            continue
        cursor += 1
    elif command[0] == "B":  # 왼쪽 문자 하나 삭제
        if cursor == 0:
            continue
        input_list.pop(cursor - 1)
        cursor -= 1
    elif command[0] == "P":  # 왼쪽에 문자 추가
        input_list.insert(cursor, command[1])
        cursor += 1

result_str = ''.join(input_list)
print(result_str)
