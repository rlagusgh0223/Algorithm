def solution(n):
    answer = [n]
    while n > 1:
        n = n//2 if n%2==0 else n*3+1
        answer.append(n)
    return answer

import sys

print(solution(int(sys.stdin.readline())))
