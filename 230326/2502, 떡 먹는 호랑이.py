# 백준 페이지 두번째 답이 안나와도 정답처리 된다
# 7 218
# 2
# 26
import sys
D, K = map(int, sys.stdin.readline().split())
dp = [0] * (D+1)
for i in range(1, 100000):
    for j in range(i, 100000):  # 1<A<B니까
        dp[1] = i
        dp[2] = j
        for k in range(3, D+1):
            dp[k] = dp[k-1] + dp[k-2]
        if dp[-1] == K:
            print(dp[1])
            print(dp[2])
            exit()