def solution(numbers):
    numbers = sorted([str(n) for n in numbers], key=lambda x:x*3, reverse=True)
    answer = int(''.join(numbers))
    return str(answer)

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
