def solution(a, b, n):
    answer = 0
    while n>=a:
        answer += (n//a)*b
        n = n - (n//a)*a + (n//a)*b
    return answer

import sys
a, b, n = map(int, sys.stdin.readline().split())
print(solution(a, b, n))