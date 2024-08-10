def solution(array, commands):
    answer = []
    for i, j, k in commands:
        # answer.append(sorted(array[i-1:j])[k-1])  # 전에는 이 한줄로 해결했다
        command = sorted(array[i-1:j])
        answer.append(command[k-1])
    return answer

import sys

array = list(map(int, sys.stdin.readline().split(", ")))
commands = list(sys.stdin.readline().split("], ["))
commands = [list(map(int, c.split(", "))) for c in commands]
print(solution(array, commands))