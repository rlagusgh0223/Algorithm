# 모든 지점에서 다른 모든 지점까지의 최단 경로를 구하는 문제는 플로이드 워셜 문제이다
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[int(1e9)]*n for _ in range(n)]

# 자기 자신에서 자기 자신으로 가는 비용은 0
for i in range(n):
    graph[i][i] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = min(c, graph[a-1][b-1])  # 노선이 하나가 아닐 경우 최소값 넣는다

# 플로이드 워셜 알고리즘
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 결과 출력
for i in range(n):
    for j in range(n):
        if graph[i][j] == int(1e9):
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()