def solution(numbers):
    return [n*2 for n in numbers]

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
