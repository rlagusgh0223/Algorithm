def solution(n):
    answer = 0
    for i in range(1, n+1):
        finn = 0
        plus = i
        while finn < n:
            finn += plus
            plus += 1
        if finn == n:
            answer += 1
    return answer

import sys
Finn = int(sys.stdin.readline())
print(solution(Finn))