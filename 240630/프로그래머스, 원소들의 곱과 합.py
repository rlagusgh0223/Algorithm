def solution(num_list):
    answer = 1
    for n in num_list:
        answer *= n
    if answer < sum(num_list)**2:
        return 1
    return 0

import sys

num_list = list(map(int, sys.stdin.readline().split(", ")))
print(solution(num_list))