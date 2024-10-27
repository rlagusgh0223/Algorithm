def solution(array):
    array.sort()
    return array[len(array)//2]

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
