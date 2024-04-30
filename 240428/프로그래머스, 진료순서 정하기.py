def solution(emergency):
    answer = [1] * len(emergency)
    for i in range(len(emergency)):
        for j in range(len(emergency)):
            if i == j:
                continue
            if emergency[i] < emergency[j]:
                answer[i] += 1
    return answer

import sys

emergency = list(map(int, sys.stdin.readline().split(", ")))
print(solution(emergency))