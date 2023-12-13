def solution(arr):
    answer = sum(arr) / len(arr)
    return answer


import sys
arr = list(map(int, sys.stdin.readline().strip().split(",")))
print(solution(arr))