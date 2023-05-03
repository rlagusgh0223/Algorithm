# c배열을 한번에 만들고 초기화 안하는게 오히려 시간 더 걸린다
# 초기화를 할 일이 많이 없어서 그런것 같다
# bfs호출할때 배열에 매개변수 안 넣으면 시간 더 오래 걸린다

def BFS():
    ok = False
    for i in range(N):
        for j in range(N):
            if c[i][j] < ans:
                c[i][j] = ans
                q = deque()
                q.append((i, j))
                s = [(i, j)]
                total = a[i][j]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0<=nx<N and 0<=ny<N and c[nx][ny]<ans:
                            if L<=abs(a[nx][ny]-a[x][y])<=R:
                                c[nx][ny] = ans
                                q.append((nx, ny))
                                s.append((nx, ny))
                                total += a[nx][ny]
                                ok = True
                val = total//len(s)
                for x, y in s:
                    a[x][y] = val
    return ok

from collections import deque
import sys
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, L, R = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0
c = [[-1]*N for _ in range(N)]
while True:
    if BFS():
        ans += 1
    else:
        break
print(ans)