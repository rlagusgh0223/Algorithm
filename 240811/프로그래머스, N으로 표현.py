def solution(N, number):
    dp = []
    for lenNum in range(1, 9):
        now = set([int(str(N)*lenNum)])
        for i in range(lenNum-1):
            for x in dp[i]:
                for y in dp[-i-1]:
                    now.add(x+y)
                    now.add(x-y)
                    now.add(x*y)
                    if y > 0:
                        now.add(x//y)
        if number in now:
            return lenNum
        dp.append(now)
    return -1

import sys

N, number = map(int, sys.stdin.readline().split())
print(solution(N, number))