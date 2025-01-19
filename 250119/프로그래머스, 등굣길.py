def solution(m, n, puddles):
    check = [[0]*(m+1) for _ in range(n+1)]
    check[1][1] = 1
    # i-1, j-1에서 값을 더해야 하므로 1부터 시작하게 한다
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 주어지기는 m, n 순서로 주어졌지만
            # 리스트는 [n, m]으로 만들어졌으므로 [j, i]로 계산한다
            if [j, i] not in puddles:
                check[i][j] += (check[i-1][j] + check[i][j-1]) % 1000000007
    return check[n][m]


import sys

m, n = map(int, sys.stdin.readline().split())
puddles = list(sys.stdin.readline().strip().split("], ["))
puddles = [list(map(int, p.split(", "))) for p in puddles]
print(solution(m, n, puddles))