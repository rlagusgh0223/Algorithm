def BFS():
    q = deque()
    q.append((0, 0))
    castle[0][0] = -1
    while q:
        x, y = q.popleft()
        if (-1*castle[x][y])-1 == T:
            continue
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx==N-1 and ny==M-1:
                return -1*castle[x][y]  # 1에서 시작했으니까 마지막으로 1 더하지 않는다
            if 0<=nx<N and 0<=ny<M:
                if castle[nx][ny] == 2:
                    castle[nx][ny] = castle[x][y] - 1
                    gram[nx][ny] = 1
                    q.append((nx, ny))
                if castle[nx][ny]==1 and gram[x][y]==1:
                    q.append((nx, ny))
                    castle[nx][ny] = castle[x][y] - 1
                if castle[nx][ny] == 0:
                    q.append((nx, ny))
                    castle[nx][ny] = castle[x][y] - 1
                if gram[nx][ny]==0 and gram[x][y]==1:  # 이전에 갔던 곳이라도 벽때문에 그람을 든 상태와 그렇지 않은 상태의 최솟값은 다를 수 있다
                    gram[nx][ny] = 1  # 이전에 그람을 들지 않고 방문한 곳이거나 처음 방문한 곳이라면 새로 계산한다
                    q.append((nx, ny))
                    castle[nx][ny] = castle[x][y] - 1
    return "Fail"

from collections import deque
import sys
N, M, T = map(int, sys.stdin.readline().split())
castle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
gram = [[0]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
print(BFS())