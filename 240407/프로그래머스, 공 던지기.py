# 모범답안
def solution(numbers, k):
    return numbers[2*(k-1) % len(numbers)]

def solutions(numbers, k):
    answer = 0
    for i in range(1, k):
        answer += 2
    answer %= len(numbers)
    return numbers[answer]

import sys

numbers = list(map(int, sys.stdin.readline().split(", ")))
k = int(sys.stdin.readline())
print(solution(numbers, k))