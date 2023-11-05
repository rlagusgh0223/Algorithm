def solution(n, left, right):
    # 다 구하면(n*n) 시간초과 나는듯
    answer = [0] * (right+1 - left)
    for i in range(left, right+1):
        answer[i-left] = max(i//n, i%n)+1
    return answer

import sys
n, left, right = map(int, sys.stdin.readline().split())
print(solution(n, left, right))