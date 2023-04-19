def BFS(i, j):
    q = deque()
    q.append((i, j))
    temp.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<12 and 0<=ny<6 and data[nx][ny]==data[x][y] and visit[nx][ny]==0:
                visit[nx][ny] = 1
                q.append((nx, ny))
                temp.append((nx, ny))

def delete(temp):
    for x, y in temp:
        data[x][y] = '.'

def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if data[k][i]=='.' and data[j][i]!='.':
                    data[k][i], data[j][i] = data[j][i], data[k][i]
                    break

from collections import deque
import sys
data = [list(sys.stdin.readline().rstrip()) for _ in range(12)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0
while True:
    ck = True
    visit = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if data[i][j]!='.' and visit[i][j]==0:
                visit[i][j] = 1
                temp = []
                BFS(i, j)
                if len(temp) >= 4:
                    ck = False
                    delete(temp)
    if ck:
        break
    down()
    ans += 1  # 여러그룹이 있다면 동시에 터지고 한번의 연쇄가 추가된다

print(ans)