def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer

import sys
arr = list(map(int, sys.stdin.readline().split(", ")))
divisor = int(sys.stdin.readline())
print(solution(arr, divisor))