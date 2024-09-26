def solution(arr1, arr2):
    if len(arr1) > len(arr2):
        return 1
    elif len(arr1) < len(arr2):
        return -1
    elif sum(arr1) > sum(arr2):
        return 1
    elif sum(arr1) < sum(arr2):
        return -1
    return 0

import sys

arr1 = list(map(int, sys.stdin.readline().split(", ")))
arr2 = list(map(int, sys.stdin.readline().split(", ")))
print(solution(arr1, arr2))