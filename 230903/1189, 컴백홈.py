def DFS(r, c, x):
    global cnt
    ground[r][c] = chr(ord('a') + x)  # 이 코드가 위에 있어야 도착지점에도 하나 증가한 알파벳을 넣는다. 문제에서 요구한건 아니지만 그냥 구분하기 위해 넣었다
    if r==0 and c==C-1 and x==K-1:
        cnt += 1
        return
    for i in range(4):
        nr, nc = r+dx[i], c+dy[i]
        if 0<=nr<R and 0<=nc<C and ground[nr][nc]=='.':
            DFS(nr, nc, x+1)
            ground[nr][nc] = '.'

import sys
R, C, K = map(int, sys.stdin.readline().split())
ground = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
DFS(R-1, 0, 0)  # r, c, 지나온 발자취
print(cnt)