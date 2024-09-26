def solution(arr, n):
    for i in range(len(arr)):
        if len(arr)%2==1 and i%2==0:
                arr[i] += n
        elif len(arr)%2==0 and i%2==1:
                arr[i] += n
    return arr

import sys

arr = list(map(int, sys.stdin.readline().split(", ")))
n = int(sys.stdin.readline())
print(solution(arr, n))