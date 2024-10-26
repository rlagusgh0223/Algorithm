def solution(num1, num2):
    return int((num1/num2) * 1000)

import sys

n1, n2 = map(int, sys.stdin.readline().split())
print(solution(n1, n2))