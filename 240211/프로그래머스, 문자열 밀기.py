def solution(A, B):
    answer = 0
    for a in range(len(A)):
        if A == B:
            return answer
        A = A[-1] + A[:-1]
        answer += 1
    return -1

import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
print(solution(A, B))