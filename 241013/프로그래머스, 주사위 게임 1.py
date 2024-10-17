def solution(a, b):
    A, B = int(a%2), int(b%2)
    if A and B:
        answer = a*a + b*b
    elif A or B:
        answer = 2 * (a+b)
    else:
        answer = abs(a - b)
    return answer

import sys

a, b = map(int, sys.stdin.readline().split())
print(solution(a, b))