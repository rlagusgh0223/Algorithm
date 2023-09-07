import sys
N = int(sys.stdin.readline())
T, P = [0 for _ in range(N+1)], [0 for _ in range(N+1)]
for i in range(1, N+1):
    T[i], P[i] = map(int, sys.stdin.readline().split())

dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i] = max(dp[i-1], dp[i])  # 오늘까지 할 수 있는 일의 최댓값
    day = i + T[i] - 1  # 앞으로 일을 하는데 필요한 날짜(지금까지 일한 날 + 일하기 위해 필요한 날 - 오늘)
    if day <= N:  # 필요한 날짜가 N일 안이라면 일할 수 있으므로
        # 며칠 후의 최댓값은 원래 가지고 있던 값과, 지금까지 일한값+오늘부터 일한 경우의 값을 비교해서 더 큰 값을 넣는다
        dp[day] = max(dp[day], dp[i-1]+P[i])
print(max(dp))