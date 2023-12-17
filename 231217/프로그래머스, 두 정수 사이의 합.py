def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    for now in range(a, b+1):
        answer += now
    return answer

import sys
a, b = map(int, sys.stdin.readline().split())
print(solution(a, b))