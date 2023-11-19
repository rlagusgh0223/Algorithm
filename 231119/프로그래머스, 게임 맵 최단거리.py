from collections import deque
def solution(maps):
    answer = -1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                if maps[nx][ny] == 1:
                    maps[nx][ny] += maps[x][y]
                    q.append((nx, ny))
    if maps[-1][-1] != 1:
        answer = maps[-1][-1]
    return answer



import sys
maps = sys.stdin.readline().strip().split("],[")
for m in range(len(maps)):
    maps[m] = list(map(int, maps[m].split(",")))
print(solution(maps))
