def solution(my_string, target):
    return 1 if target in my_string else 0

import sys

m = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
print(solution(m, t))