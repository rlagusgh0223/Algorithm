# 음수가 없다고 했으므로 첫 경우의 수는 무조건 0~20이며, 경우의 수는 더하면 된다
# 이전 순서에서 가지고 있는 경우의 수 중에 더하거나 뺐을때 0~20이면 이전 경우의 수를 더하면 된다
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
# dp[몇번째][현재까지의 수] = 가능한 경우의 수
dp = [[0]*21 for _ in range(N)]  # 숫자의 개수 N번동안 0~20이 만들어지는 경우의 수
dp[0][arr[0]] = 1
for i in range(1, N-1):  # 마지막 수는 연산 결과니까 연산에 들어갈 일이 없다
    for j in range(21):
        if dp[i-1][j]:  # 이 앞의 순서에서 올 경우의 수가 있었다면
            # 이번 수와 이전 까지 수의 합이 0~20 사이라면 이번 수의 경우의 수 더한다
            if j+arr[i]<=20:
                dp[i][j+arr[i]] += dp[i-1][j]
            if j-arr[i]>=0:
                dp[i][j-arr[i]] += dp[i-1][j]
print(dp[N-2][arr[N-1]])