def BFS(X, Y):
    q = deque()
    q.append((0, 0))
    visit = [[0]*Y for _ in range(X)]  # 나이트가 뒤로는 못 가니까 X, Y보다 앞으로 나가는건 계산할 필요 없다
    visit[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(2):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<X and 0<=ny<Y:
                visit[nx][ny] += (visit[x][y] % (10**9+7))
                q.append((nx, ny))
    return visit[X-1][Y-1]


from collections import deque
import sys
TC = int(sys.stdin.readline())
dx = [1, 2]
dy = [2, 1]
for t in range(TC):
    X, Y = map(int, sys.stdin.readline().split())
    ans = BFS(X+1, Y+1)
    print("#{} {}".format(t+1, ans))