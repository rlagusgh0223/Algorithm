def solution(n):
    answer = 0
    for i in range(1, n+1):
        ck = 0
        for j in range(1, i+1):
            if i%j == 0:
                ck += 1
        if ck >= 3:
            answer += 1
    return answer

import sys

print(solution(int(sys.stdin.readline())))
