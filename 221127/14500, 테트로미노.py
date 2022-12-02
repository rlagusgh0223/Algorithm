# 시간초과 나므로 그전의 코드 쓰는게 나을 것 같다
def go(x, y, sum, cnt):
    if cnt == 4:
        global ans
        if ans < sum:
            ans = sum
        return
    if x<0 or x>=N or y<0 or y>=M:
        return
    if c[x][y]:
        return
    c[x][y] = True
    for i in range(4):
        go(x+dx[i], y+dy[i], sum+a[x][y], cnt+1)
    c[x][y] = False

import sys
N, M = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
c = [[False]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0
for i in range(N):
    for j in range(M):
        go(i, j, 0, 0)
        if j+2 < M:
            temp = a[i][j] + a[i][j+1] + a[i][j+2]
            if i-1 >= 0:
                temp2 = temp + a[i-1][j+1]
                if ans < temp2:
                    ans = temp2
            if i+1 < N:
                temp2 = temp + a[i+1][j+1]
                if ans < temp2:
                    ans = temp2
        if i+2 < N:
            temp = a[i][j] + a[i+1][j] + a[i+2][j]
            if j-1 >= 0:
                temp2 = temp + a[i+1][j-1]
                if ans < temp2:
                    ans = temp2
            if j+1 < M:
                temp2 = temp + a[i+1][j+1]
                if ans < temp2:
                    ans = temp2
print(ans)