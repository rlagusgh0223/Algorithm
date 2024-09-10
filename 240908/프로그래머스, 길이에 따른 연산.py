def solution(num_list):
    answer = 1
    if len(num_list) <= 10:
        for n in num_list:
            answer *= n
    else:
        answer = sum(num_list)
    return answer

import sys

num_list = list(map(int, sys.stdin.readline().split(", ")))
print(solution(num_list))