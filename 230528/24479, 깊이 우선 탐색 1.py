def DFS(i):
    global cnt
    E[i] = cnt
    for now in V[i]:
        if E[now] == 0:
            cnt += 1
            DFS(now)

import sys
sys.setrecursionlimit(10**6)  # 재귀 함수 깊이 지정하는 함수로 이거 안쓰면 에러난다
N, M, R = map(int, sys.stdin.readline().split())
V = [[] for _ in range(N)]
E = [0] * N
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    u, v = u-1, v-1
    V[u].append(v)
    V[v].append(u)
for i in range(N):
    V[i].sort()
cnt = 1
DFS(R-1)
for ans in E:
    print(ans)