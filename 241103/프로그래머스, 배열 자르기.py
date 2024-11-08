def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

import sys

n = list(map(int, sys.stdin.readline().split(", ")))
n1, n2 = map(int, sys.stdin.readline().split())
print(solution(n, n1, n2))