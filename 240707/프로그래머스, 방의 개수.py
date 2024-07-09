from collections import defaultdict


def solution(arrows):
    answer = 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    visit = defaultdict(list)
    x, y = 0, 0  # 현재 좌표(시작은 0, 0에서 한다)
    for a in arrows:
        # 대각선 이동으로 인한 교차점이 있는지 확인하기 위해 두 번 나누어 처리한다
        # 대각선으로만 이어져 있고 방이 없다면 두번째 반복문에서
        # (nx, ny) in visit and (x, y) not in visit[(nx, ny)]
        # 조건에 맞지 않아 answer가 늘지 않는다
        for _ in range(2):
            nx, ny = x+dx[a], y+dy[a]
            # 다음 좌표가 방문한 적이 있지만 현재 점과 이어지지 않은 경우 방이 생긴다
            if (nx, ny) in visit and (x, y) not in visit[(nx, ny)]:
                answer += 1
                visit[(nx, ny)].append((x, y))
                visit[(x, y)].append((nx, ny))
            # 다음 좌표를 방문한 적 자체가 없는 경우 방문 목록에 넣는다
            elif (nx, ny) not in visit:
                visit[(nx, ny)].append((x, y))
                visit[(x, y)].append((nx, ny))
            x, y = nx, ny

    return answer

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
