def solution(sides):
    sides.sort()
    return 1 if sides[0]+sides[1] > sides[2] else 2

import sys

sides = list(map(int, sys.stdin.readline().split(", ")))
print(solution(sides))