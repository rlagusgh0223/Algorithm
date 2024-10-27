def solution(arr):
    answer = [arr[0]]
    for a in arr:
        if answer[-1] != a:
            answer.append(a)
    return answer

import sys

print(solution(list(map(int, sys.stdin.readline().split(",")))))
