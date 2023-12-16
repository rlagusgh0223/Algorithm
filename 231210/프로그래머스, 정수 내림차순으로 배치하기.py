def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    return int(''.join(answer))


import sys
n = int(sys.stdin.readline())
print(solution(n))