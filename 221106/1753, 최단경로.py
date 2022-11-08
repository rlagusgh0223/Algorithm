def stra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        wei, now = heapq.heappop(heap)
        if wei > dp[now]:
            continue
        for next_v, w in graph[now]:
            next_w = w + wei
            if next_w < dp[next_v]:
                dp[next_v] = next_w
                heapq.heappush(heap, (next_w, next_v))

import sys, heapq
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
heap = []
INF = sys.maxsize
dp = [INF]*(V+1)
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
stra(K)
for i in range(1, V+1):
    print("INF" if dp[i]==INF else dp[i])


# heap      (0, 1)          (2, 2)          (3, 3)      (7, 4)
# wei       0               2               3           7
# now       1               2               3           4(4에는 입력값 없으므로 종료)
# next_w    2       3       3       4       4
# w         2       3       4       5       6
# next_w    0+2     0+3     (2+4)   2+5     (3+6)