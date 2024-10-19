def solution(arr, k):
    if k%2 == 1:
        return [a*k for a in arr]
    else:
        return [a+k for a in arr]

import sys

arr = list(map(int, sys.stdin.readline().split(", ")))
k = int(sys.stdin.readline())
print(solution(arr, k))