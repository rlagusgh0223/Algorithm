import sys
input = sys.stdin.readline
while True:
    ck = True
    now = list(map(int, list(input().rstrip())))
    if now[0]==0:
        break
    for i in range(len(now)//2):
        if now[i] != now[len(now)-1-i]:
            ck = False
            break
    if ck:
        print("yes")
    else:
        print("no")