def solution(n):
    return [N for N in range(1, n+1, 2)]

import sys

print(solution(int(sys.stdin.readline())))
