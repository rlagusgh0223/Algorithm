def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]

import sys

a = list(map(int, sys.stdin.readline().split(", ")))
c = list(sys.stdin.readline().strip().split("], ["))
c = [list(map(int, C.split(", "))) for C in c]
print(solution(a, c))