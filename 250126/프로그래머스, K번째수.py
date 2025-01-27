def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]

import sys

a = list(map(int, sys.stdin.readline().split(", ")))
commands = list(sys.stdin.readline().strip().split("], ["))
commands = [list(map(int, c.split(", "))) for c in commands]
print(solution(a, commands))