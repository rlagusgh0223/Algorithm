def solution(num1, num2):
    answer = num1*num2
    return answer

import sys
num1, num2 = map(int, sys.stdin.readline().split())
print(solution(num1, num2))