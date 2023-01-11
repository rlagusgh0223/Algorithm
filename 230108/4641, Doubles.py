import sys
while True:
    lst = list(map(int, sys.stdin.readline().split()))
    if lst[0] == -1:
        break
    lst.pop()
    cnt = 0
    for i in range(len(lst)):
        if 2*lst[i] in lst:
            cnt += 1
    print(cnt)