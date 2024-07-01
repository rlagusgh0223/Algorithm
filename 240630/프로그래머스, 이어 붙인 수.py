def solution(num_list):
    odd, even = '', ''
    for n in num_list:
        if n%2 == 0:
            even += str(n)
        else:
            odd += str(n)
    return int(odd) + int(even)

import sys

num_list = list(map(int, sys.stdin.readline().split(", ")))
print(solution(num_list))