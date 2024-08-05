def solution(my_string, m, c):
    return my_string[c-1::m]

import sys

my_string = sys.stdin.readline().strip()
m, c = map(int, sys.stdin.readline().split())
print(solution(my_string, m, c))