# 누적합을 이용해서 풀어야 된다
# 이차원 배열을 이용해서 풀면 시간초과 난다
import sys
N, M = map(int, sys.stdin.readline().split())
ground = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
sumg = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        sumg[i][j] = ground[i-1][j-1] - sumg[i-1][j-1] + sumg[i-1][j] + sumg[i][j-1]
for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(sumg[x2][y2] + sumg[x1-1][y1-1] - sumg[x1-1][y2] - sumg[x2][y1-1])