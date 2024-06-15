def solution(a, b):
    return max(2*a*b, int(f"{a}{b}"))

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
print(solution(a, b))