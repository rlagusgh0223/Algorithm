import sys
t = int(sys.stdin.readline())
for _ in range(t):
    ck = input()
    cnt = 0
    r, c = map(int, sys.stdin.readline().split())
    candy = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
    for i in range(r):
        for j in range(1, c-1):
            if candy[i][j-1]=='>' and candy[i][j]=='o' and candy[i][j+1]=='<':
                cnt += 1
    for j in range(c):
        for i in range(1, r-1):
            if candy[i-1][j]==chr(118) and candy[i][j]=='o' and candy[i+1][j]==chr(94):
                cnt += 1
    print(cnt)