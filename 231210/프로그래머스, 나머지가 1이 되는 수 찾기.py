def solution(n):
    for x in range(2, n):
        if n%x == 1:
            return x

import sys
n = int(sys.stdin.readline())
print(solution(n))