# 1차원 배열 누적합
# DP[i] = DP[i-1] + DP[i]
# 누적합을 이용해서 i ~ j 값 구하기
# DP[j] = DP[j] - DP[i-1]

# 2차원 배열 누적합
# 왼쪽, 위의 값을 더하고 대각선 왼쪽 위의 값을 뺀다
# DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + A[i][j]
# 누적합을 이용해서 i,j ~ x,y 값 구하기
# DP[x][u] = DP[x][y] - DP[i-1][y] - DP[x][j-1] + DP[i-1][j-1]
# DP[i-1][j-1]은 두번 뺀 경우가 되니 한번 더해준다

N, M = map(int, input().split())
A = [[0] for _ in range(N+1)]
A[0] += [0] * M
for i in range(1, N+1):
    A[i] += list(map(int, input().split()))
DP = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + A[i][j]

K = int(input())
for i in range(K):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[i-1][y] - DP[x][j-1] + DP[i-1][j-1])