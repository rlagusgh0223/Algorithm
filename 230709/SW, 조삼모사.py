# https://www.codetree.ai/training-field/frequent-problems/problems/three-at-dawn-and-four-at-dusk/description?page=1&pageSize=20
# 답은 잘 나오지만 메모리 초과
import sys, itertools
n = int(sys.stdin.readline())
work = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
P = list(itertools.permutations(list(range(n))))
ans = 1e9
for now in P:
    X = Y = 0
    x, y = list(now[:n//2]), list(now[n//2:])
    for i in x:
        for j in x:
            if i == j:
                continue
            X += work[i][j]
    for i in y:
        for j in y:
            if i == j:
                continue
            Y += work[i][j]
    ans = min(ans, abs(X-Y))
print(ans)