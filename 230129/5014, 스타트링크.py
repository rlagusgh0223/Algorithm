# 속도를 나름 줄여보려고 ux, dx마다 G가 되는 즉시 종료하게 했는데 오히려 시간이 더 걸린다
def bfs(S):
    q = deque()
    q.append(S)
    ck = [-1] * (F+1)
    ck[S] = 0
    while q:
        x = q.popleft()
        if x == G:
            return ck[x]
        ux, dx = x+U, x-D
        if 1<=ux<=F and ck[ux]==-1:
            ck[ux] = ck[x] + 1
            q.append(ux)
        if 1<=dx<=F and ck[dx]==-1:
            ck[dx] = ck[x] + 1
            q.append(dx)
    return "use the stairs"

from collections import deque
import sys
F, S, G, U, D = map(int, sys.stdin.readline().split())
print(bfs(S))