def solution(n):
    answer = 1
    i = 1
    while answer*i <= n:
        answer *= i
        i += 1
    return i-1

import sys

print(solution(int(sys.stdin.readline())))
