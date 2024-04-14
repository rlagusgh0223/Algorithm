def solution(arr):
    answer = 0
    while True:
        ck = True
        for i in range(len(arr)):
            if arr[i]>=50 and arr[i]%2==0:
                arr[i] //= 2
                ck = False
            elif arr[i]<50 and arr[i]%2==1:
                arr[i] = arr[i]*2 + 1
                ck = False
        if ck:
            break
        answer += 1
    return answer

import sys

arr = list(map(int, sys.stdin.readline().split(", ")))
print(solution(arr))