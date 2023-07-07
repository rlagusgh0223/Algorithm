# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYgEu2460GwDFARP
# 문제에서 체스판의 크기를 지정해 주지 않았다
# 말이 뒤로 가지는 않으므로 주어진 값이 끝이라고 가정해서 판을 만들어 보았으나 값이 큰 경우 답이 안 나온다
# 3
# 3 3
# #1 2
# 2 2
# #2 0
# 999999 999999
# 여기서 값이 안 나온다 
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