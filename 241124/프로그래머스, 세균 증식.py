def solution(n, t):
    return n*(2**t)

import sys

n, t = map(int, sys.stdin.readline().split())
print(solution(n, t))