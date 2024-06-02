def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

import sys

array = list(map(int, sys.stdin.readline().split(", ")))
commands = list(sys.stdin.readline().split("], ["))
commands = [list(map(int, c.split(", "))) for c in commands]
print(solution(array, commands))