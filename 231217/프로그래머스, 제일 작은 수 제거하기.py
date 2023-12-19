def solution(arr):
    answer = []
    amin = min(arr)
    for a in arr:
        if a != amin:
            answer.append(a)
    if len(answer) == 0:
        answer = [-1]
    return answer


import sys
arr = list(map(int, sys.stdin.readline().split(",")))
print(solution(arr))