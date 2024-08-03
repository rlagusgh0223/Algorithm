def solution(my_string, is_suffix):
    answer = [my_string[i:] for i in range(len(my_string))]
    if is_suffix in answer:
        return 1
    return 0

import sys

my_string = sys.stdin.readline().strip()
is_suffix = sys.stdin.readline().strip()
print(solution(my_string, is_suffix))