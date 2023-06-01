def dijk(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        now, dist = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

import heapq, sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
distance = [INF] * (N+1)

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

start, end = map(int, sys.stdin.readline().split())

dijk(start)
print(distance[end])