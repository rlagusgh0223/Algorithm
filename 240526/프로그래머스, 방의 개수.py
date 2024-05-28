from collections import defaultdict


def solution(arrows):
    answer = 0
    visit = defaultdict(list)  # 연결된 좌표를 저장할 리스트
    x, y = 0, 0
    # dx, dy 좌표는 문제의 그림 보면 나온다
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    for a in arrows:
        # 대각선의 교차점을 정확하게 확인하기 위해 2번 돌린다
        for _ in range(2):
            nx, ny = x+dx[a], y+dy[a]
            # 방문한 적 있는 좌표이고, 현재 좌표와 연결된 적이 없다면
            # 이제 방이 하나 만들어진거다
            if (nx, ny) in visit and (x, y) not in visit[(nx, ny)]:
                answer += 1
                visit[(x, y)].append((nx, ny))
                visit[(nx, ny)].append((x, y))
            # 방문한 적이 없는 좌표면 현재 좌표와 연결된걸 표시한다
            elif (nx, ny) not in visit:
                visit[(x, y)].append((nx, ny))
                visit[(nx, ny)].append((x, y))
            x, y = nx, ny
    return answer

import sys

arrows = list(map(int, sys.stdin.readline().split(", ")))
print(solution(arrows))