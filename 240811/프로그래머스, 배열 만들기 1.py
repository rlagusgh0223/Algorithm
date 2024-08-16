def solution(n, k):
    answer = [i for i in range(1, n+1) if i%k==0]
    return answer

import sys

n, k = map(int, sys.stdin.readline().split())
print(solution(n, k))
