# 시간초과 줄이기 위해 
# 1) input -> sys.stdin.readline()
# 2) insert/del -> append/pop

# 기존 시간초과 코드
import sys
string = sys.stdin.readline().strip()
cmd_count = int(sys.stdin.readline().strip())
cursor = len(string)

for _ in range(cmd_count):
    cmd = sys.stdin.readline().strip()
    if cmd == "L":
        if cursor == 0: continue
        cursor -= 1
    elif cmd == "D":
        if cursor == len(string): continue
        cursor += 1
    elif cmd == "B":
        if cursor == 0: continue
        cursor -= 1
        string = list(string)
        del string[cursor] # 시간복잡도 O(N) -> pop 사용 O(1)
        string = "".join(string)
    else:
        cmd = cmd.replace(" ","")
        char = cmd[1:]
        string = list(string)
        string.insert(cursor, char) # 시간복잡도 O(N) -> append 사용 O(1)
        string = "".join(string)
        cursor += 1
print(string)