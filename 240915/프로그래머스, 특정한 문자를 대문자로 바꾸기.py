def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())

import sys

my = sys.stdin.readline().strip()
alp = sys.stdin.readline().strip()
print(solution(my, alp))