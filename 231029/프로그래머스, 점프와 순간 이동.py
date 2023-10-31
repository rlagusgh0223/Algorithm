def solution(n):
    # 건전지를 적게 쓰기 위해선 X2로 갈 수 있는 만큼 가는게 좋다
    # 도착지점에서부터 역순으로 돌아온다
    answer = 0
    while n>0:
        if n%2 == 0:
            n //= 2
        else:
            n -= 1
            answer += 1
    return answer

    # 효율성 테스트에서 떨어진다
    # dp = [int(1e9)] * (n+1)
    # dp[0] = 0
    # for i in range(1, n+1):
    #     dp[i] = min(dp[i-1]+1, dp[i])
    #     if i*2 <= n:
    #         dp[i*2] = min(dp[i*2], dp[i])
    # return dp[n]

    # 그런데 위의 과정 다 필요없고
    # 이진수로 바꿔서 1만 세주면 원하는 답이 나온다고 한다
    # return bin(n).count('1')

import sys
n = int(sys.stdin.readline())
print(solution(n))