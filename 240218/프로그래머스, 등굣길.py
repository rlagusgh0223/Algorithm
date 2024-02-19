def solution(m, n, puddles):
    # n, m이 주어진 순서와 좌표가 다르므로 puddles도 좌표를 바꿔줘야 한다
    puddles = [[y, x] for x, y in puddles]
    board = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:
                board[i][j] = 1
            elif [i, j] not in puddles:
                # 오른쪽, 아래쪽으로 갈 수 있다고 했으므로
                # 왼쪽, 위에서 오는 길의 수를 더하면 해당 좌표로 오는 경로 수를 알 수 있다
                board[i][j] = (board[i-1][j] + board[i][j-1]) % 1000000007
    return board[n][m]

import sys

m, n = map(int, sys.stdin.readline().split())
puddles = list(sys.stdin.readline().strip().split("], ["))
puddles = [list(map(int, p.split(", "))) for p in puddles]
print(solution(m, n, puddles))