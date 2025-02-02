from collections import defaultdict


def solution(arrows):
    answer = 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    room = defaultdict(list)
    x, y = 0, 0
    for i in arrows:
        for _ in range(2):
            nx, ny = x+dx[i], y+dy[i]
            if (nx, ny) not in room:
                room[(nx, ny)].append((x, y))
                room[(x, y)].append((nx, ny))
            elif (x, y) not in room[(nx, ny)]:
                answer += 1
                room[(nx, ny)].append((x, y))
                room[(x, y)].append((nx, ny))
            x, y = nx, ny
    return answer

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
