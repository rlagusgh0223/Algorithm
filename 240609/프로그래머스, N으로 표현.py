def solution(N, number):
    dp = []
    # N의 최솟값이 8보다 크면 -1 리턴
    for i in range(1, 9):
        # N을 i번 반복해서 만들 수 있는 수의 집합
        now = set([int(str(N)*i)])
        # i=1  => dp[1]
        # i=2  => dp[0]과 dp[1], 또는 dp[1]과dp[0]의 조합
        # i=3  => dp[0]과 dp[2], dp[1]과 dp[1], dp[2]와 dp[0]의 조합
        # 각 dp에는 이전 계산한 수들의 집합이 있다
        for j in range(i-1):
            for x in dp[j]:
                for y in dp[-j-1]:
                    now.add(x+y)
                    now.add(x-y)
                    now.add(x*y)
                    if y > 0:
                        now.add(x//y)
        # 이번 수의 조합에 목표하는 수가 있다면 i번의 수로 만들 수 있으므로 리턴
        if number in now:
            return i
        # 아니면 다음 연산을 위해 dp에 이번 조합 입력
        dp.append(now)
    return -1

import sys

N, number = map(int, sys.stdin.readline().split())
print(solution(N, number))