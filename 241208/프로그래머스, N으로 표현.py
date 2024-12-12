def solution(N, number):
    dp = []
    for num in range(1, 9):
        now = set([int(str(N)*num)])
        for i in range(num-1):
            for x in dp[i]:
                # dp를 앞, 뒤 한번씩 싹 계산하려고 하는것 같다
                for y in dp[-i-1]:
                    now.add(x+y)
                    now.add(x-y)
                    now.add(x*y)
                    if y>0:
                        now.add(x//y)
        if number in now:
            return num
        dp.append(now)
    return -1

import sys

N, number = map(int, sys.stdin.readline().split())
print(solution(N, number))