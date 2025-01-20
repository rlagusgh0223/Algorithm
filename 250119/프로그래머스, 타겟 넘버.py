from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((numbers[0], 1))
    q.append((-numbers[0], 1))
    while q:
        num, cnt = q.popleft()
        if cnt==len(numbers):
            if num == target:
                answer += 1
        else:
            q.append((num + numbers[cnt], cnt+1))
            q.append((num - numbers[cnt], cnt+1))
    return answer

import sys

numbers = list(map(int, sys.stdin.readline().split(", ")))
target = int(sys.stdin.readline())
print(solution(numbers, target))