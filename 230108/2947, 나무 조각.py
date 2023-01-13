import sys
lst = list(map(int, sys.stdin.readline().split()))
while True:
    ck = True
    for i in range(1, 5):
        if lst[i-1] > lst[i]:
            lst[i-1], lst[i] = lst[i], lst[i-1]
            print(*lst, sep=' ')
            ck = False
    if ck:
        break