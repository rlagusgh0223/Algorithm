def solution(A, B):
    answer, a, b = 0, 0, 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    # A의 리스트에서 현재 B의 값보다
    # 작은값이 나올때까지 B의 위치값을 유지하고 비교한다
    for _ in range(len(A)):
        if A[a] < B[b]:
            answer += 1
            b += 1
        a += 1
    return answer

import sys

A = list(map(int, sys.stdin.readline().split(",")))
B = list(map(int, sys.stdin.readline().split(",")))
print(solution(A, B))