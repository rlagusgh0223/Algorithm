def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)


import sys

x1, x2, x3, x4 = sys.stdin.readline().strip().split()
print(solution(x1, x2, x3, x4))