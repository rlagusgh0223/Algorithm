def solution(array, n):
    return array.count(n)

import sys

a = list(map(int, sys.stdin.readline().split(", ")))
n = int(sys.stdin.readline())
print(solution(a, n))