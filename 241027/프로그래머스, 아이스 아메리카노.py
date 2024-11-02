def solution(money):
    return [money//5500, money%5500]

import sys

print(solution(int(sys.stdin.readline())))
