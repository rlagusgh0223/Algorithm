def solution(arr):
    a = len(arr)
    ar = len(arr[0])
    if a > ar:
        for i in range(a):
            for j in range(a-ar):
                arr[i].append(0)
    elif a < ar:
        for i in range(ar - a):
            arr.append([0]*ar)
    return arr

import sys

arr = list(sys.stdin.readline().split("], ["))
arr = [list(map(int, a.split(", "))) for a in arr]
print(solution(arr))