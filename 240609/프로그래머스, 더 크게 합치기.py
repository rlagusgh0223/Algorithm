def solution(a, b):
    return max(int(str(a)+str(b)), int(str(b)+str(a)))

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
print(solution(a, b))