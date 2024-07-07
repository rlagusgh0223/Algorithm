def solution(m, n, puddles):
    check = [[0]*(m+1) for _ in range(n+1)]
    check[1][1] = 1  # 출발지 초기값은 1로 둔다
    for i in range(1, n+1):
        for j in range(1, m+1):
            # puddles에는 [m, n]값으로 입력됐지만
            # 실제 리스트는 [n, m]으로 만들어졌으므로
            # 좌표 바꿔서 비교한다
            if [j, i] not in puddles:
                check[i][j] += (check[i-1][j] + check[i][j-1]) % 1000000007
    return check[n][m]

import sys

m, n = map(int, sys.stdin.readline().split())
puddles = list(sys.stdin.readline().strip().split("], ["))
puddles = [list(map(int, p.split(", "))) for p in puddles]
print(solution(m, n, puddles))