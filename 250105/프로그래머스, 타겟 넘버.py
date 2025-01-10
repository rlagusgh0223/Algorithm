from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0, 0))
    dx = [1, -1]
    while q:
        cnt, now = q.popleft()
        if cnt == len(numbers):
            if now == target:
                answer += 1
        else:
            for x in dx:
                q.append((cnt+1, now + x*numbers[cnt]))
    return answer

import sys

numbers = list(map(int, sys.stdin.readline().split(", ")))
target = int(sys.stdin.readline())
print(solution(numbers, target))


# from collections import deque


# def solution(numbers, target):
#     answer = 0
#     q = deque()
#     q.append((0, 0))
#     n = len(numbers)
#     while q:
#         idx, number = q.popleft()
#         if idx==n and number==target:
#             answer += 1
#         elif idx < n:
#             q.append((idx+1, number+numbers[idx]))
#             q.append((idx+1, number-numbers[idx]))
#     return answer