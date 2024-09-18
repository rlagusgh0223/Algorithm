def solution(my_string):
    return [ms for ms in my_string.strip().split()]

import sys

print(solution(sys.stdin.readline()))
