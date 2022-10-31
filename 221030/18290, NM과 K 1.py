import sys
N, M, K = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
c = [[False]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = -10000  # 이거보다 작으면 답은 나오는데 틀렸다고 한다

def go(px, py, cnt, sum):
    if cnt == K:
        global ans
        if ans < sum:
            ans = sum
        return
    for x in range(px, N):
        for y in range(py if x==px else 0, M):  # 원래는 py+1부터 시작해야 되지만
            if c[x][y]:  # 어차피 이 코드에 의해 py는 동작하지 않는다
                continue
            ok = True
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<N and 0<=ny<M:
                    if c[nx][ny]:
                        ok = False
            if ok:
                c[x][y] = True
                go(x, y, cnt+1, sum+lst[x][y])
                c[x][y] = False
go(0, 0, 0, 0)
print(ans)