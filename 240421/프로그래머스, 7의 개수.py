def solution(array):
    return str(array).count('7')

import sys

array = list(map(int, sys.stdin.readline().split(", ")))
print(solution(array))