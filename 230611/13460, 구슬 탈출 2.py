def BFS(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by, 0))
    visit = []
    visit.append((rx, ry, bx, by))
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt > 10:
            return -1
        if ball[rx][ry] == 'O':  # 구멍에 빨간공이 들어가면 횟수 반환
            return cnt
        for i in range(4):
            nrx, nry, nbx, nby = rx, ry, bx, by
            # 빨간공이 한쪽 방향으로 끝까지 가게 함
            while True:
                nrx, nry = nrx+dx[i], nry+dy[i]
                if ball[nrx][nry] == '#':  # 현재 위치가 벽이라면 한 칸 뒤로 물러나서 이동 가능한 곳으로 공의 위치를 옮긴다
                    nrx, nry = nrx-dx[i], nry-dy[i]
                    break
                if ball[nrx][nry] == 'O':  # 구멍에 빠진다면 이번 턴은 끝
                    break
            # 파란공이 한쪽 방향으로 끝까지 가게 함
            while True:
                nbx, nby = nbx+dx[i], nby+dy[i]
                if ball[nbx][nby] == '#':
                    nbx, nby = nbx-dx[i], nby-dy[i]
                    break
                if ball[nbx][nby] == 'O':
                    break
            # 파란공이 구멍에 들어간 경우는 어차피 계산할 필요가 없다
            if ball[nbx][nby] == 'O':
                continue
            # 두 공의 위치가 같다면 더 나중에 온 공이 한 칸 뒤로 간다
            if nrx==nbx and nry==nby:
                if abs(nrx-rx)+abs(nry-ry) > abs(nbx-bx)+abs(nby-by):
                    nrx, nry = nrx-dx[i], nry-dy[i]
                else:
                    nbx, nby = nbx-dx[i], nby-dy[i]
            # 방문한 적이 없다면 큐에 입력하고 방문 체크
            if (nrx, nry, nbx, nby) not in visit:
                q.append((nrx, nry, nbx, nby, cnt+1))
                visit.append((nrx, nry, nbx, nby))
    return -1  # 아직 10번을 넘기진 않았지만 구멍으로 나갈 수 없을 때

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
ball = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(N):
    for j in range(M):
        if ball[i][j] == 'R':
            rx, ry = i, j
        elif ball[i][j] == 'B':
            bx, by = i, j
print(BFS(rx, ry, bx, by))