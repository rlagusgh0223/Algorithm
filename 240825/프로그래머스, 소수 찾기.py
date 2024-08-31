from itertools import permutations


def solution(numbers):
    answer = 0
    num = []

    for i in range(1, len(numbers)+1):
        num += list(permutations(numbers, i))
    num = list(set(int(''.join(n)) for n in num))
    
    for n in num:
        ck = True
        if n < 2:
            continue
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                ck = False
                break
        if ck:
            answer += 1
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
