import sys
n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]  # 해당 금액을 만드는 경우의 수를 저장하는 배열
dp = [0] * (k+1)
dp[0] = 1  # 코인을 하나만 쓰는 경우를 위해
# ex) 1원일땐 1원 하나는 가능하므로 dp[1-1] = dp[0] = 1
#     2원이 되기 위해서는 최소한 2원 자체 한번은 가능하므로 dp[2-2] = dp[0] = 1
#     5원이 되기 위해서는 최소한 5원 자체 한번은 가능하므로 dp[5-5] = dp[0] = 1
for coin in coins:
    # coin원 동전으로 i원 만들기 = i - coin원을 만든 후 coin원을 추가
    # 즉, i-coin과 경우의 수는 같다
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]
print(dp[k])