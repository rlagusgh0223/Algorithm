def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

import sys
a = list(map(int, sys.stdin.readline().split(",")))
b = list(map(int, sys.stdin.readline().split(",")))
print(solution(a, b))