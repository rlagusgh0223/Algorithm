def solution(num1, num2):
    return 1 if num1==num2 else -1

import sys

n1, n2 = map(int, sys.stdin.readline().split())
print(solution(n1, n2))