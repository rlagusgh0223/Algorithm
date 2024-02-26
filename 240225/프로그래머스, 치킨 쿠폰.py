def solution(chicken):
    answer = 0
    while chicken >= 10:
        div, mod = chicken//10, chicken%10
        answer += div
        chicken = div + mod
    return answer

import sys

print(solution(int(sys.stdin.readline())))
