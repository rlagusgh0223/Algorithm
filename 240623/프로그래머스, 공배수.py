def solution(number, n, m):
    return int(number%n == number%m == 0)

import sys

number, n, m = map(int, sys.stdin.readline().split())
print(solution(number, n, m))