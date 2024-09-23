def solution(rny_string):
    return rny_string.replace('m', 'rn')

import sys

print(solution(sys.stdin.readline().strip()))
