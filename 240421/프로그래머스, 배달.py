from sys import maxsize


def solution(N, road, K):
    # 방문 했는지 체크하는 리스트, 각 마을 방문 최소 시간 리스트, 방문 가능한 마을 및 시간 리스트
    visit, cost, way = [0]*(N+1), [maxsize]*(N+1), [[] for _ in range(N+1)]
    for r in road:
        way[r[0]].append((r[1], r[2]))
        way[r[1]].append((r[0], r[2]))
    # 1번 마을에서 K 시간 안에 배달 가능한 마을의 수를 구하는 것이므로
    # 1번 마을이 비용은 0이다
    cost[1] = 0

    # 1번 마을에서 각 마을까지 최소 시간 갱신
    for _ in range(1, N+1):
        Min = maxsize
        for i in range(1, N+1):
            # 마을에 방문한 적이 없고, 최소 시간이라면 Min과 방문했다고 표시할 곳(b) 갱신
            if visit[i]==0 and cost[i]<Min:
                Min = cost[i]
                b = i
        visit[b] = 1

        # 모든 길을 돌면서 최소 시간 갱신
        for n, nt in way[b]:
            # 기존 시간(cost[n]) 보다 새로운 시간(cost[b]+nt)이 더 작으면 시간 갱신
            if cost[n] > cost[b] + nt:
                cost[n] = cost[b] + nt
    return len([c for c in cost if c<=K])

import sys

N, K = map(int, sys.stdin.readline().split())
road = list(sys.stdin.readline().strip().split("],["))
road = [list(map(int, now.split(","))) for now in road]
print(solution(N, road, K))