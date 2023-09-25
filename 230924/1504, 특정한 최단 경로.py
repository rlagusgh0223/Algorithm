# 두 정점을 지나가는 최단경로는 아래 두가지 경우 중 하나
# 시작정점 -> stop1 -> stop2 -> 도착정점
# 시작정점 -> stop2 -> stop1 -> 도착정점
def dijkstra(start, end):
    dis = [1e9] * (N+1)  # 누적 거리 저장할 리스트
    dis[start] = 0
    q = [[0, start]]  # heap연산은 리스트에 하므로 처음에는 그냥 리스트로 선언해주면 된다. [첫 정점까지의 거리, 첫 정점]
    while q:
        # heappop은 가장 작은 원소를 지운다. 즉, 이전 정점에서 가장 가까운 현재 정점을 k, u에 넣는다
        dist, now = heappop(q)  # 이전 정점에서 현재 정점까지의 거리, 현재 정점
        if dist > dis[now]:
            continue
        for w, nxt in G[now]:
            if dis[nxt] > dis[now] + w:
                dis[nxt] = dis[now] + w
                heappush(q, [dis[now], nxt])
    return dis[end]



import sys
from heapq import heappush, heappop

N, E = map(int, sys.stdin.readline().split())
G = [[] for _ in range(N+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    # [다음 정점으로의 거리, 다음 정점]
    G[u].append([w, v])
    G[v].append([w, u])
stop1, stop2 = map(int, sys.stdin.readline().split())

# 1 -> stop1 -> stop2 -> N
path1 = dijkstra(1, stop1) + dijkstra(stop1, stop2) + dijkstra(stop2, N)
# 1 -> stop2 -> stop1 -> N
path2 = dijkstra(1, stop2) + dijkstra(stop2, stop1) + dijkstra(stop1, N)

if path1>=1e9 and path2>=1e9:
    print(-1)
else:
    print(min(path1, path2))