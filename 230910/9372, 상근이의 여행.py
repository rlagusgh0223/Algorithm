# 어차피 모든 국가는 연결되어 있으므로(신장트리) N-1번 움직이면 된다
# 그러나 문제에서 원하는건 이런 풀이가 아니었을 것이기 때문에 그냥 참고만 할 것
# import sys
# T = int(sys.stdin.readline())
# for _ in range(T):
#     N, M = map(int, sys.stdin.readline().split())
#     for _ in range(M):
#         a, b = map(int, sys.stdin.readline().split())
#     print(N-1)



import sys

def DFS(node, cnt):
    check[node] = 1
    for now in graph[node]:
        if check[now] == 0:
            cnt = DFS(now, cnt+1)
    return cnt

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    check = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    print(DFS(1, 0))