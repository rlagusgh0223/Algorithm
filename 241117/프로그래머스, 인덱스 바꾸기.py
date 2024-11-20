def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    return ''.join(my_string)

import sys

s = sys.stdin.readline().strip()
n1, n2 = map(int, sys.stdin.readline().split())
print(solution(s, n1, n2))