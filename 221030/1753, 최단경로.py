import sys
import heapq

def stra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        wei, now = heapq.heappop(heap)
        if wei < dp[now]:
            continue
        for next_v, w in graph[now]:
            next_wei = w + wei
            if next_wei < dp[next_v]:
                dp[next_v] = next_wei
                heapq.heappush(heap, (next_wei, next_v))

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
INF = sys.maxsize
dp = [INF] * (V+1)
heap = []
graph = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
stra(K)
for i in range(1, V+1):
    print("INF" if dp[i]==INF else dp[i])