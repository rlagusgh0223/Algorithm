def solution(num1, num2):
    return num1 % num2

import sys

n1, n2 = map(int, sys.stdin.readline().split())
print(solution(n1, n2))
