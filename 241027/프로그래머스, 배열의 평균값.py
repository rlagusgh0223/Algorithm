def solution(numbers):
    return sum(numbers) / len(numbers)

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
