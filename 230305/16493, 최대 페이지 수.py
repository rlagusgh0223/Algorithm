# knapsack문제다
import sys
N, M = map(int, sys.stdin.readline().split())
dp = [[0]*(N+1) for _ in range(M+1)] # 가능/불가능의 여부를 결정하는게 이차원 배열 안쪽으로 들어와야 된다
for i in range(1, M+1):
    day, page = map(int, sys.stdin.readline().split())
    for j in range(1, N+1):
        if j-day < 0:  # 1. 남은일수보다 많은 일수를 써야한다면 읽지 않는다
            dp[i][j] = dp[i-1][j]
        else:  # 2. 그렇지 않다면, 다음 중 더 나은 가치를 선택한다
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-day]+page)  # 3. 이전 값 그대로 가지고 간다 / 현재 필요한 날짜만큼 빼고 읽는 페이지수를 추가한다.
print(dp[M][N])