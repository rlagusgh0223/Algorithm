import sys
R, C = map(int, sys.stdin.readline().split())
ck = [0]*5
p = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
for i in range(R-1):
    for j in range(C-1):
        if p[i][j]=='#' or p[i+1][j]=='#' or p[i][j+1]=='#' or p[i+1][j+1]=='#':
            continue
        cnt = 0
        if p[i][j] == 'X':
            cnt += 1
        if p[i+1][j] == 'X':
            cnt += 1
        if p[i][j+1] == 'X':
            cnt += 1
        if p[i+1][j+1] == 'X':
            cnt += 1
        ck[cnt] += 1
print(*ck, sep='\n')