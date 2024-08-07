def solution(my_string, is_prefix):
    answer = [my_string[:i+1] for i in range(len(my_string))]
    return 1 if is_prefix in answer else 0

import sys

my_string = sys.stdin.readline().strip()
is_prefix = sys.stdin.readline().strip()
print(solution(my_string, is_prefix))