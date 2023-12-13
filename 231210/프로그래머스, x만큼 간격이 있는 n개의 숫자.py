def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer


import sys
x, n = map(int, sys.stdin.readline().split())
print(solution(x, n))