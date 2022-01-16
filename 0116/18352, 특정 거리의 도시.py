from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().split())

# 입력된 그대로 리스트에 반영하기 위해 리스트를 한칸씩 더 만든다. 나중에 append를 위해 []로 선언
graph = [[] for _ in range(N+1)]
# 거리를 측정할 겸 만약 방문했던 도시면 다시 방문하지 않도록 하기 위한 리스트
check = [0 for _ in range(N+1)]

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)      # graph에서는 []로 선언했으니까 필요한 곳에만 값을 추가할 수 있다

def BFS(x):
    q = deque()            
    q.append((x, 1))
    while q:
        x, cnt = q.popleft()        # 도시, 도시 거리를 check에 입력하기 위한 변수
        for i in graph[x]:          # 해당 도시에서 연결된 도시가 있는지 확인(리스트에 값이 있으면 연결, 없으면 무시)
            if check[i] == 0:       # 연결된 도시는 그냥 리스트에 있는거니까 과거 방문한 적이 있는지만 체크
                check[i] = cnt
                q.append((i, cnt+1))         # 연결된 도시가 있다면 q에 입력해서 다음 연산을 하도록 수행

check[X] = -1           # 혹시라도 출발지를 목적지로 만들어서 check상에 해당 도시 거리가 나오는걸 방지
BFS(X)

for i in range(N+1):
    if check[i] == K:
        check[0] = 1    # 조건에 맞아서 출력한 곳이 있다면 표시. check[0]은 어차피 편의를 위해 만들어둔거니까 0으로 있을거다
        print(i)        # 어차피 도시순서대로 입력되어 있으니까 오름차순으로 출력된다

if check[0] == 0:       # 해당 거리의 도시가 없는 경우 -1 출력
    print('-1')