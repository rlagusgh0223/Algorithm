import sys
N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 0

while True:
    if a[r][c] == 0:
        a[r][c] = 2
    if a[r-1][c]!=0 and a[r+1][c]!=0 and a[r][c+1]!=0 and a[r][c-1]!=0:
        if a[r-dr[d]][c-dc[d]] == 1:
            break
        else:
            r, c = r-dr[d], c-dc[d]
    else:
        d = (d+3) % 4
        if a[r+dr[d]][c+dc[d]] == 0:
            r, c = r+dr[d], c+dc[d]

for i in range(N):
    for j in range(M):
        if a[i][j] == 2:
            cnt += 1
print(cnt)