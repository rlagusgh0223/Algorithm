def solution(n):
    if n <= 2:
        return 0
    before = now = 1
    for _ in range(2, n+1, 2):
        before, now = now, (4*now - before) % 1000000007
    return now

import sys

print(solution(int(sys.stdin.readline())))
