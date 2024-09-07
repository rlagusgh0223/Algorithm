def solution(numbers, n):
    answer = 0
    for i in range(len(numbers)):
        answer += numbers[i]
        if answer > n:
            return answer

import sys

numbers = list(map(int, sys.stdin.readline().split(", ")))
n = int(sys.stdin.readline())
print(solution(numbers, n))