from itertools import permutations


def check(num):
    if num < 2:
        return 0
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return 0
    return 1

def solution(numbers):
    answer = 0
    number = []
    for i in range(1, len(numbers)+1):
        number += list(permutations(numbers, i))
    number = list(set(int(''.join(n)) for n in number))
    for num in number:
        answer += check(num)
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
