# 시작점과 도착점이 하나로 정해져 있고 최단 거리를 구하는 문제면 다익스트라 문제라고 생각해볼것
import sys, heapq
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr[-1] = 0

INF = sys.maxsize

# 양방향 그래프 연결
connect = [[] for _ in range(N)]
for i in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    connect[a].append((t, b))
    connect[b].append((t, a))

# 다익스트라
def dijkstra(start, end):
    dis_list = [INF for _ in range(N)]
    dis_list[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        dis, node = heapq.heappop(pq)
        # 갱신된게 더 작을 경우에는 넘어감
        if dis > dis_list[node]:
            continue
        # 다음 노드의 거리가 새롭게 생긴 다음 노드의 거리보다 크고
        # 다음 노드가 방문할 수 있는 노드인 경우에 거리 업데이트하고 pq에 넣어줌
        for next_cost, next_node in connect[node]:
            if dis_list[next_node] > dis_list[node]+next_cost and not arr[next_node]:
                dis_list[next_node] = dis_list[node] + next_cost
                heapq.heappush(pq, (dis_list[next_node], next_node))
    return dis_list[end]

num = dijkstra(0, N-1)
if num == INF:
    print(-1)
else:
    print(num)