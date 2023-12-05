from collections import deque
def solution(maps):
    answer = []
    check = [[0]*len(maps[0]) for _ in range(len(maps))]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    maps = [list(map) for map in maps]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]!='X' and check[i][j]==0:
                q.append((i, j))
                now = int(maps[i][j])
                check[i][j] = now
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny]!='X' and check[nx][ny]==0:
                            now += int(maps[nx][ny])
                            check[nx][ny] = now
                            q.append((nx, ny))
                answer.append(now)
                
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)


import sys
maps = list(sys.stdin.readline().strip().split('","'))
print(solution(maps))