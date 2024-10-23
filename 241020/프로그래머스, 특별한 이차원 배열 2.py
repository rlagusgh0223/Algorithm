def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1

import sys

arr = list(sys.stdin.readline().strip().split("], ["))
arr = [list(map(int, a.split(", "))) for a in arr]
print(solution(arr))