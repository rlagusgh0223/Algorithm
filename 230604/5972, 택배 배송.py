def dijkstra():
    q = []
    # 무슨 원리인지는 모르겠는데 비용을 앞에 두고 목적지를 뒤에 둬야 시간 이 더 빠른다
    heapq.heappush(q, (0, 1))  # 1번 곳간에 필요한 여물은 0
    weed[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > weed[now]:  # 최솟값을 구하는데 여기서부터 커버리면 밑은 계산하는 의미가 없다
            continue
        for nxt in cow[now]:  # 현재 곳간과 연결된 다른 곳간들 확인
            cost = nxt[1] + dist
            if cost < weed[nxt[0]]:  # 현재 곳간을 거쳐 다른 곳간으로 가는 여물이 더 적은 경우
                weed[nxt[0]] = cost
                heapq.heappush(q, (cost, nxt[0]))

import heapq, sys
N, M = map(int, sys.stdin.readline().split())
cow = [[] for _ in range(N+1)]
weed = [1e9] * (N+1)
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    cow[A].append((B, C))
    cow[B].append((A, C))
dijkstra()
print(weed[N])