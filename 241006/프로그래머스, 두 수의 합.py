def solution(a, b):
    return str(int(a)+int(b))

import sys

a, b = sys.stdin.readline().split()
print(solution(a, b))