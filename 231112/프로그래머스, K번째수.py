def solution(array, commands):
    answer = []
    for x, y, z in commands:
        lst = array[x-1:y]
        lst.sort()
        answer.append(lst[z-1])
    return answer

import sys
array = list(map(int, sys.stdin.readline().split(", ")))
commands = list(sys.stdin.readline().strip().split("], ["))
commands = [list(map(int, now.split(', '))) for now in commands]
print(solution(array, commands))