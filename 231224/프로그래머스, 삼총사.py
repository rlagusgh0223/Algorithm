from itertools import combinations
def solution(number):
    answer = 0
    student = combinations(number, 3)
    for st in student:
        if sum(st) == 0:
            answer += 1
    return answer


import sys
num = list(map(int, sys.stdin.readline().split(', ')))
print(solution(num))