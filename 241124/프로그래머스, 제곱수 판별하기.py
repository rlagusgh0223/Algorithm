def solution(n):
    return 1 if n**0.5 == int(n**0.5) else 2

import sys

print(solution(int(sys.stdin.readline())))
