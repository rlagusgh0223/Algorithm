def solution(n):
    return sum([i for i in range(2, n+1, 2)])

import sys

print(solution(int(sys.stdin.readline())))
