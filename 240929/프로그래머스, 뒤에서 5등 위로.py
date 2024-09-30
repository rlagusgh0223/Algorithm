def solution(num_list):
    return sorted(num_list)[5:]

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
