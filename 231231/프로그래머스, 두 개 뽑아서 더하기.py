from itertools import combinations
def solution(numbers):
    answer = set()
    numbers = combinations(numbers, 2)
    for num in numbers:
        answer.add(sum(num))
    return sorted(list(answer))

import sys
num = list(map(int, sys.stdin.readline().split(",")))
print(solution(num))