def dfs(x, c):
    color[x] = c
    for y in graph[x]:
        if color[y] == 0:
            if not dfs(y, 3-c):
                return False
        elif color[x] == color[y]:
            return False
    return True

import sys
sys.setrecursionlimit(1000000)
K = int(sys.stdin.readline())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V)]
    color = [0] * V
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    ans = True
    for i in range(V):
        if color[i] == 0:
            if not dfs(i, 1):
                ans = False
    print("YES" if ans else "NO")