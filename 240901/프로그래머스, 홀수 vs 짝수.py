def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
