def solution(n):
    answer = 0
    x = n**0.5
    if x%1 == 0:
        answer = int(x+1)**2
    else:
        answer = -1
    return answer


import sys
n = int(sys.stdin.readline())
print(solution(n))