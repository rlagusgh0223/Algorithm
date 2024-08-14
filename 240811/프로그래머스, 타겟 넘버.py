from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0, 0))
    while q:
        idx, cnt = q.popleft()
        if idx==len(numbers) and cnt==target:
            answer += 1
        if idx < len(numbers):
            q.append((idx+1, cnt+numbers[idx]))
            q.append((idx+1, cnt-numbers[idx]))
    return answer

import sys

numbers = list(map(int, sys.stdin.readline().split(", ")))
target = int(sys.stdin.readline())
print(solution(numbers, target))