def solution(i, j, k):
    answer = 0
    k = str(k)
    for n in range(i, j+1):
        n = str(n)
        if k in n:
            answer += n.count(k)
    return answer

import sys

i, j, k = map(int, sys.stdin.readline().split())
print(solution(i, j, k))