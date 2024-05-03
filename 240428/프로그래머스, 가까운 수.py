def solution(array, n):
    array.sort()
    answer = [abs(a-n) for a in array]
    return array[answer.index(min(answer))]


import sys

array = list(map(int, sys.stdin.readline().split(", ")))
n = int(sys.stdin.readline())
print(solution(array, n))