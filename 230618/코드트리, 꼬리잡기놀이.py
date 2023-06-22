# https://www.codetree.ai/training-field/frequent-problems/problems/tail-catch-play/description?page=3&pageSize=20
# 1 ~ n : 오른쪽
# n+1 ~ 2n : 위
# 2n+1 ~ 3n : 왼쪽
# 3n+1 ~ 4n : 아래
# 방향으로 공 던지는거 반복
# 해당 줄에 처음으로 만나는 사람의 점수**2만큼 점수 얻음
# 점수 획득 후 방향 바꿈
# 공을 한 번 던질 때 마다 한 칸씩 전진함

# 해야되는것
# 1. 머리/꼬리 사람 바꾸기
# 2. 앞으로 한 칸 전진
def BFS(i, j):
    q = deque()
    q.append((i, j))
    visit[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and 0<ground[nx][ny]<4 and visit[nx][ny]==0:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))

from collections import deque
import sys
n, m, k = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j]==0 and ground[i][j]==1:
            BFS(i, j)
for i in range(n):
    print(visit[i])
while k > 0:
    for i in range(4*n):  # 오른쪽으로
        ck = False
        if i < n:
            print(i, k)
            for j in range(n):
                if 0 < ground[i][j] < 4:
                    ans += visit[i][j]**2
                    print(visit[i][j])
                    k -= 1
                    ck = True
                    break
            if not ck:
                k -= 1
                    # 1과 3의 위치 바꾸고 방향 바꾼 후 한칸 전진
        elif i<2*n and not ck:  # 위로
            print(i, k)
            for j in range(n-1, -1, -1):
                if 0 < ground[j][i-n] < 4:
                    ans += visit[j][i-n]**2
                    k -= 1
                    ck = True
                    break
            if not ck:
                k -= 1
        elif i<3*n and not ck:  # 왼쪽으로
            print(i, k)
            I = 1
            for j in range(n-1, -1, -1):
                if 0 < ground[n-I][j] < 4:
                    ans += visit[n-I][j]**2
                    k -= 1
                    ck = True
                    break
                I += 1
            if not ck:
                k -= 1
        elif i<4*n and not ck:  # 아래로
            print(i, k)
            if i == 3*n:
                I = n-1
            for j in range(n):
                if 0 < ground[j][I] < 4:
                    ans += visit[j][I]**2
                    k -= 1
                    ck = True
                    break
            if not ck:
                k -= 1
                I -= 1
print(ans)













# check = [[0]*n for _ in range(n)]
# k = 0
# I = 1
# for i in range(4*n):  # 오른쪽으로
#     if i < n:
#         for j in range(n):
#             check[i][j] = k
#             k += 1
#         for i in range(n):
#             print(check[i])
#         print("--------")
#     elif i < 2*n:  # 위로
#         for j in range(n-1, -1, -1):
#             check[j][i-n] = k
#             k += 1
#         for i in range(n):
#             print(check[i])
#         print("--------")
#     elif i < 3*n:  # 왼쪽으로
#         for j in range(n-1, -1, -1):
#             check[n-I][j] = k
#             k += 1
#         I += 1
#         for i in range(n):
#             print(check[i])
#         print("--------")
#     else:  # 아래로
#         if I >= n:
#             I = n-1
#         for j in range(n):
#             check[j][I] = k
#             k += 1
#         I -= 1
#         for i in range(n):
#             print(check[i])
#         print("--------")