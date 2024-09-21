def solution(binomial):
    answer = 0
    a, op, b = binomial.split()
    a, b = int(a), int(b)
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    elif op == '*':
        answer = a * b
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
