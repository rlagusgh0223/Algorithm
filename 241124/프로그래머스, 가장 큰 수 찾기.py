def solution(array):
    answer = []
    answer.append(max(array))
    answer.append(array.index(answer[0]))
    return answer

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
