def solution(N, number):
    dp = []
    # 8을 넘어가면 -1을 리턴하라고 했으므로 8까지만 계산한다
    for i in range(1, 9):
        now = set([int(str(N)*i)])
        # dp[3]은 N*3, (dp[1]연산dp[2]), (dp[2]연산dp[1]) 로 되어 있다
        for j in range(i-1):
            for first in dp[j]:
                for second in dp[-j-1]:
                    now.add(first+second)
                    now.add(first-second)
                    now.add(first*second)
                    if second > 0:
                        now.add(first//second)
        # 이번 사칙연산의 결과가 계산에 있으면 i(자릿수) 출력
        if number in now:
            return i
        dp.append(now)
    return -1

import sys
N, number = map(int, sys.stdin.readline().split())
print(solution(N, number))