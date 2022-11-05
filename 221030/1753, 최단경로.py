def bfs(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        wei, now = heapq.heappop(heap)
        if wei < dp[now]:
            continue
        for next_v, w in graph[now]:
            next_w = w + wei
            if next_w < dp[next_v]:
                dp[next_v] = next_w
                heapq.heappush(heap, (next_w, next_v))

import sys, heapq
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
INF = sys.maxsize
heap = []
graph = [[] for _ in range(V+1)]
dp = [INF] * (V+1)
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
bfs(K)
for i in range(1, V+1):
    print("INF" if dp[i]==INF else dp[i])