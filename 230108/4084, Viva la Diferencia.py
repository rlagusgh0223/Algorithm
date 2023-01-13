import sys
while True:
    a, b, c, d = map(int, sys.stdin.readline().split())
    if a==b==c==d==0:
        break
    cnt = 0
    while True:
        if a==b==c==d:
            break
        cnt += 1
        a, b, c, d = abs(a-b), abs(b-c), abs(c-d), abs(d-a)
    print(cnt)