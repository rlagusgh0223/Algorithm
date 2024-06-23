def solution(num, n):
    return 1 if num%n==0 else 0

import sys

num, n = map(int, sys.stdin.readline().split())
print(solution(num, n))