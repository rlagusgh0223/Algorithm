def solution(num_list, n):
    return 1 if n in num_list else 0

import sys

num = list(map(int, sys.stdin.readline().split(", ")))
n = int(sys.stdin.readline())
print(solution(num, n))