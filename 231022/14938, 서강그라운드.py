# 데이크스트라 보다는 플로이드 워셜에 어울리는 문제 같다
# 그러나 데이크스트라 유형을 찾다가 나온 문제이므로 데이크스트라로 푼다
def dijkstra(start):
    q = []
    distance = [int(1e9)] * (n+1)
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for nxt, ndist in graph[now]:
            cost = dist + ndist
            if distance[nxt] > cost:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))
    temp = 0
    for i in range(1, n+1):
        if distance[i] <= m:
            temp += item[i]
    return temp

import heapq, sys
n, m, r = map(int, sys.stdin.readline().split())
item = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a].append((b, l))
    graph[b].append((a, l))
ans = 0
for i in range(1, n+1):
    ans = max(ans, dijkstra(i))
print(ans)