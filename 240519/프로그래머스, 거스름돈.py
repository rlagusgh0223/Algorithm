def solution(n, money):
    dp = [1] + [0] * n  # 각 동전으로 만들 수 있는 경우의 수
    for m in money:  # 주어진 동전들을 모두 사용
        # 현재 주어진 동전보다 큰 가격의 경우의 수에 계산
        for price in range(m, n+1):
            if price >= m:
                # 현재 가격의 경우의 수에 지금 동전만큼 이전의 값을 더한다
                # ex) 현재 가격은 5원인데, 동전이 2원인 경우
                # 2원 전인 3원일 때의 경우의 수 만큼 5원이 될 수 있다.
                # 3원에 2원을 더하면 5원이기 때문이다.
                dp[price] += dp[price-m]
    return dp[n] % 1000000007

import sys

n = int(sys.stdin.readline())
money = list(map(int, sys.stdin.readline().split(",")))
print(solution(n, money))