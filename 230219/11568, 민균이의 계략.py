import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dp = [1] * N
for i in range(N):
    for j in range(i+1, N):
        if lst[i]<lst[j] and dp[i]>=dp[j]:
            dp[j] = dp[i]+1
print(max(dp))