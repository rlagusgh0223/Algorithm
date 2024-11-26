def solution(n, numlist):
    return [num for num in numlist if num%n==0]

import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split(", ")))
print(solution(n, num))