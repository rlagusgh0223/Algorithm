def solution(numbers, direction):
    if direction == 'left':
        numbers = numbers[1:] + [numbers[0]]
    else:
        numbers = [numbers[-1]] + numbers[:-1]
    return numbers

import sys

n = list(map(int, sys.stdin.readline().split(", ")))
d = sys.stdin.readline().strip()
print(solution(n, d))