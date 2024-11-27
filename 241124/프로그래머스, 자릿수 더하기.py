def solution(n):
    return sum(list(map(int, str(n))))

import sys

print(solution(int(sys.stdin.readline())))
