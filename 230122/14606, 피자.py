# 다이나믹 프로그래밍
import sys
N = int(sys.stdin.readline())
dp = [0] * 11
dp[2] = 1
for i in range(3, N+1):
    k = i//2
    dp[i] = k*(i-k) + dp[k] + dp[i-k]
print(dp[N])

# 내가 생각한 코딩
# import sys
# N = int(sys.stdin.readline())
# ans = 0
# while N > 1:
#     N -= 1
#     ans += N
# print(ans)