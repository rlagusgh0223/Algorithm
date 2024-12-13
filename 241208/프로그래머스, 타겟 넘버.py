from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0, 0))
    n = len(numbers)
    while q:
        idx, number = q.popleft()
        if idx==n and number==target:
            answer += 1
        elif idx < n:
            q.append((idx+1, number+numbers[idx]))
            q.append((idx+1, number-numbers[idx]))
    return answer

import sys

n = list(map(int, sys.stdin.readline().split(", ")))
t = int(sys.stdin.readline())
print(solution(n, t))