# n개의 지역이 있으며
# roads를 통해 연결된 지역을 알 수 있다
# sources에는 강철부대원들이 있고
# destination으로 이동 가능한 최단거리를 리스트에 입력해서
# 모든 강철부대원들의 최단거리를 리스트로 출력한다
# 연결되어 있지 않다면 -1 리턴

# 강철부대 각각의 위치에서 destination까지의 거리 계산하면 시간초과 나온다
# destination에서 연결 가능한 모든곳을 파악한 후,
# 강철부대원과의 거리를 리스트에 입력한다
from collections import deque


def solution(n, roads, sources, destination):
    answer = [-1] * (n+1)  # destination에서 떨어진 거리를 입력할 리스트
    visit = [[] for _ in range(n+1)]  # 각 지역이 연결되어 있는 경로 확인하는 리스트
    
    # 연결된 지역들을 저장할 이차원 리스트
    for x, y in roads:
        visit[x].append(y)
        visit[y].append(x)

    # BFS를 이용해 destination에서 각 지역으로의 최단거리를 구한다
    q = deque()
    q.append(destination)
    answer[destination] = 0
    while q:
        x = q.popleft()
        for nx in visit[x]:
            if answer[nx] == -1:
                answer[nx] = answer[x] + 1
                q.append(nx)

    # destination에서 각 지역으로의 최단거리가 입력된
    # 리스트에서 강철부대원까지의 거리를 반환한다
    return [answer[s] for s in sources]

import sys

n = int(sys.stdin.readline())
roads = list(sys.stdin.readline().strip().split("], ["))
roads = [list(map(int, road.split(", "))) for road in roads]
sources = list(map(int, sys.stdin.readline().split(", ")))
destination = int(sys.stdin.readline())
print(solution(n, roads, sources, destination))