def solution(num_list, n):
    return num_list[::n]

import sys

lst = list(map(int, sys.stdin.readline().split(", ")))
n = int(sys.stdin.readline())
print(solution(lst, n))