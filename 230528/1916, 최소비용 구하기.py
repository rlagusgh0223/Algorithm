def dijk(start):
    q = []
    # 시작 노드로 가기 위한 최소 비용은 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 저렴한 값을 가지고 있는 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 지금 가지고 있는 값보다 더 작은 값이 있다면(더 최적의 값이 있다면) 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:  # i[도착지, 비용]
            cost = dist + i[1]  # 현재 비용과 연결된 곳의 비용의 합
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 저렴한 경우
            if cost < distance[i[0]]:  # 지금 나온 값이 기존의 값보다 저렴하다면
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

import heapq, sys
INF = int(1e9)  # 10억
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]
distance = [INF] * (N+1)

# 모든 버스(간선) 정보 받기
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())  # 출발, 도착, 가격
    graph[a].append((b, c))

start, end = map(int, sys.stdin.readline().split())

dijk(start)
print(distance[end])