def solution(my_string):
    answer = sorted(list(my_string.lower()))
    return ''.join(answer)

import sys

print(solution(sys.stdin.readline().strip()))
