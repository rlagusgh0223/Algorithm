def solution(n, results):
    pro = [[0]*n for _ in range(n)]
    for win, lose in results:
        pro[win-1][lose-1] = 1
        pro[lose-1][win-1] = -1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j or pro[i][j] in [1, -1]:
                    continue
                if pro[i][k]==pro[k][j]==1:
                    pro[i][j] = 1
                    pro[k][i] = pro[j][k] = pro[j][i] = -1
    return sum(1 for p in pro if p.count(0)==1)

import sys

n = int(sys.stdin.readline())
results = list(sys.stdin.readline().strip().split("], ["))
results = [list(map(int, r.split(", "))) for r in results]
print(solution(n, results))