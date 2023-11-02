def solution(n):
    answer = [1, 2] + [0] * (n-2)
    for i in range(2, n):
        answer[i] = (answer[i-1] + answer[i-2]) % 1234567
    return answer[n-1]

import sys
n = int(sys.stdin.readline())
print(solution(n))