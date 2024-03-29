def solution(arr, k):
    answer = []
    for a in arr:
        if a not in answer:
            answer.append(a)
        if len(answer) == k:
            break
    if len(answer) < k:
        answer += [-1 for _ in range(k-len(answer))]
    return answer

import sys

arr = list(map(int, sys.stdin.readline().split(", ")))
k = int(sys.stdin.readline())
print(solution(arr, k))