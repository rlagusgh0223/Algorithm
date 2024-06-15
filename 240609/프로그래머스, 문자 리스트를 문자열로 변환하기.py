def solution(arr):
    return ''.join(arr)

import sys

arr = list(sys.stdin.readline().strip().split('","'))
print(solution(arr))