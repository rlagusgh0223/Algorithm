def solution(n):
    return [i for i in range(1, n+1) if n%i==0]

import sys

print(solution(int(sys.stdin.readline())))
