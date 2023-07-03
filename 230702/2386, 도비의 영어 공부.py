import sys
while True:
    lst = list(sys.stdin.readline().rstrip())
    if lst[0] == '#':
        break
    now = lst[0]  # 문제에서 소문자를 입력한다고 주어졌으므로 이건 소문자다
    cnt = lst[1:].count(now) + lst[1:].count(now.upper())
    print(lst[0], cnt)