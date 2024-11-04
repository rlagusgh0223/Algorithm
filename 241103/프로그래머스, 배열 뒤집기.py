def solution(num_list):
    return num_list[::-1]

import sys

print(solution(list(map(int, sys.stdin.readline().strip().split(", ")))))
