def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1

import sys

arr = list(map(int, sys.stdin.readline().split(", ")))
idx = int(sys.stdin.readline())
print(solution(arr, idx))