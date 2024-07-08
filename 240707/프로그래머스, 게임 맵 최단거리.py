from collections import deque


# 5x5로 고정된게 아니라 예시만 그렇게 준 것 같다
# 코드를 5x5로 맞춰서 작성하면 에러 나온다
def solution(maps):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny]==1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
    if maps[-1][-1] == 1:
        return -1
    return maps[-1][-1]

import sys

maps = list(sys.stdin.readline().strip().split("],["))
maps = [list(map(int, m.split(","))) for m in maps]
print(solution(maps))