from collections import deque
def bfs(start, end, maps):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    visit = [[-1]*len(maps[0]) for i in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == start:
                q.append([i, j])
                visit[i][j] = 0
                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        nx ,ny = x+dx[i], y+dy[i]
                        if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                            if maps[nx][ny]!='X' and visit[nx][ny]==-1:
                                q.append([nx, ny])
                                visit[nx][ny] = visit[x][y] + 1
                                if maps[nx][ny] == end:
                                    return visit[nx][ny]
    return -1

# 레버를 거친다고 했으므로 출발점에서 레버까지 가는 최소거리와
# 레버에서 도착점까지 가는 최소거리의 합을 구하면 된다
def solution(maps):
    # 출발점에서 레버로 가는 최소 거리
    result1 = bfs('S', 'L', maps)
    # 레버에서 도착점으로 가는 최소 거리
    result2 = bfs('L', 'E', maps)
    if result1!=-1 and result2!=-1:
        return result1 + result2
    return -1

import sys
maps = list(sys.stdin.readline().strip().split('","'))
maps = [list(map) for map in maps]
print(solution(maps))