def solution(arr, delete_list):
    for d in delete_list:
        if d in arr:
            arr.pop(arr.index(d))
    return arr

import sys

arr = list(map(int, sys.stdin.readline().split(", ")))
de = list(map(int, sys.stdin.readline().split(", ")))
print(solution(arr, de))