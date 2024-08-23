def solution(arr, intervals):
    answer = []
    for a, b in intervals:
        answer += arr[a:b+1]
    return answer

import sys

arr = list(map(int, sys.stdin.readline().split(", ")))
intervals = list(sys.stdin.readline().strip().split("], ["))
intervals = [list(map(int, i.split(", "))) for i in intervals]
print(solution(arr, intervals))