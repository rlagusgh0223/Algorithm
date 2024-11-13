def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]

import sys

n = list(map(int, sys.stdin.readline().split(", ")))
print(solution(n))