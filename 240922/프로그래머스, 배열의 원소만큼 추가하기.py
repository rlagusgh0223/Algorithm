def solution(arr):
    return [a for a in arr for i in range(a)]

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
