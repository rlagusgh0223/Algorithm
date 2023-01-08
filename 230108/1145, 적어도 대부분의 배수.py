import sys
lst = list(map(int, sys.stdin.readline().split()))
ck = min(lst)
while True:
    cnt = 0
    for i in range(5):
        if ck%lst[i]==0:
            cnt += 1
    if cnt > 2:
        print(ck)
        break
    ck += 1