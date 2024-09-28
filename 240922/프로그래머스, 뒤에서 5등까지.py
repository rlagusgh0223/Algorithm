def solution(num_list):
    num_list.sort()
    return num_list[:5]

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
