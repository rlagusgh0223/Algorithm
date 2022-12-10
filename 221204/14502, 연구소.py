# 해당 코드는 pypy3로 해야 시간초과 안나옴
def dfs(ground):
    # 받은 그래프 check로 복사
    check = [[0]*M for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(M):
            check[i][j] = ground[i][j]
            if check[i][j] == 2:
                q.append((i, j))
    # 바이러스 전파
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and check[nx][ny]==0:
                check[nx][ny] = 2
                q.append((nx, ny))
    # 안전구역 계산
    cnt = 0
    for i in range(N):
        for j in range(M):
            if check[i][j] == 0:
                cnt += 1
    # 안전구역 반환
    return cnt

from collections import deque
N, M = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0
for i1 in range(N):
    for j1 in range(M):
        if ground[i1][j1] != 0:
            continue
        for i2 in range(N):
            for j2 in range(M):
                if ground[i2][j2] != 0:
                    continue
                for i3 in range(N):
                    for j3 in range(M):
                        if ground[i3][j3] != 0:
                            continue
                        if i1==i2 and j1==j2:
                            continue
                        if i2==i3 and j2==j3:
                            continue
                        if i1==i3 and j1==j3:
                            continue
                        ground[i1][j1] = 1
                        ground[i2][j2] = 1
                        ground[i3][j3] = 1
                        now = dfs(ground)
                        if ans < now:
                            ans = now
                        ground[i1][j1] = 0
                        ground[i2][j2] = 0
                        ground[i3][j3] = 0
print(ans)