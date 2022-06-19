import sys
n = int(sys.stdin.readline())
wine=[0 for _ in range(n+1)]
for i in range(n):
  wine[i] = int(sys.stdin.readline())

dp = [0]
dp.append(wine[0])
dp.append(wine[0] + wine[1])

for i in range(3, n+1):
  dp.append(max(dp[i-1], wine[i-1]+dp[i-2], wine[i-1]+wine[i-2]+dp[i-3]))
print(dp[n])