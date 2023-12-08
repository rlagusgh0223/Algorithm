# 카탈란수열
# 이진트리, 삼각형 갯수 구하기, 계산 순서 구하기 등
# 개수를 구하는 많은 문제의 해답이 될 수 있다
# Cn = C0*Cn-1 + C1*Cn-2 + ... Cn-1*C0
def solution(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
    return dp[n]

import sys
n = int(sys.stdin.readline())
print(solution(n))