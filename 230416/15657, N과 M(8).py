# N = 4, M = 2라고 할 때
# idx    now
# 0       0
# 0       1
# 0       2
# 0       3
# 1       1
# 1       2
# 1       3
# 2       2
# 2       3
# 3       3

def DFS(depth, idx):
    if depth == M:
        print(*ans, sep=' ')
        return
    for now in range(idx, N):
        ans[depth] = lst[now]  # depth번째의 자리에는 앞 자리의 수 이후 값만 입력된다
        DFS(depth+1, now)

import sys
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
ans = [0] * M
DFS(0, 0)