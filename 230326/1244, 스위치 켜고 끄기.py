import sys
s = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    cnt = 1
    if x == 1:
        while y*cnt <= s:
            lst[y*cnt-1] = (lst[y*cnt-1]+1)%2
            cnt += 1
    elif x == 2:
        lst[y-1] = (lst[y-1]+1) % 2
        while True:
            if y-cnt<1 or y+cnt>s:
                break
            if lst[y-cnt-1]==lst[y+cnt-1]:
                lst[y-cnt-1] = (lst[y-cnt-1]+1) % 2
                lst[y+cnt-1] = (lst[y+cnt-1]+1) % 2
                cnt += 1
            else:
                break
for i in range(s):
    if i>=20 and i%20==0:
        print()
    print(lst[i],end=' ')