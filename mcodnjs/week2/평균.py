C = int(input())
for i in range(C):
    string = input().split()
    string = list(map(int, string))
    num = string[0]
    avg = sum(string[1:], 0.0)/num
    pct = 0
    for score in string[1:]:
        if score > avg: pct += 1
    pct = pct / num * 100
    print("{:.3f}%".format(pct))