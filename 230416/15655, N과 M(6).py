def DFS(depth, idx):
    if depth == M:
        print(*ans, sep=' ')
        return
    for i in range(idx, N):
        if visit[i] == 0:
            visit[i] = 1
            ans[depth] = lst[i]
            DFS(depth+1, i+1)
            visit[i] = 0

import sys
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
visit = [0] * N
ans = [0] * M
DFS(0, 0)