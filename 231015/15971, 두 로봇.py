# 지금까지 모든 통로의 합 - 지금까지 방문한 통로 중 가장 큰 통로값 을 구해야 된다
def BFS(start, end):
    q = deque()
    q.append((start, 0, 0))  # 출발 위치, 지금까지 모든 통로의 합, 통로 중 가장 큰 값
    visit = [False] * (N+1)
    visit[start] = True
    while q:
        now, total, ncost = q.popleft()
        if now == end:
            print(total - ncost)
            return
        for nxt, cost in lst[now]:
            if visit[nxt] == False:
                visit[nxt] = True
                q.append((nxt, total+cost, max(ncost, cost)))

from collections import deque
import sys
N, start, end = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, sys.stdin.readline().split())
    lst[a].append((b, c))
    lst[b].append((a, c))
BFS(start, end)  # 원래 매개변수 안줘도 되지만 어차피 BFS에서 사용하니까 선언해줬다