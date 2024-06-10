from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque()
    # 첫번째 값을 넣으려면 -인 상태도 또 넣어야 해서
    # 그냥 아무 계산도 하지 않은 idx=-1, cnt=0값을 입력했다
    q.append((-1, 0))  # 순서, 수들의 합
    while q:
        idx, cnt = q.popleft()
        if idx==len(numbers)-1 and cnt==target:
            answer += 1
        elif idx+1 < len(numbers):
            q.append((idx+1, cnt+numbers[idx+1]))
            q.append((idx+1, cnt-numbers[idx+1]))
    return answer

import sys

numbers = list(map(int, sys.stdin.readline().split(", ")))
target = int(sys.stdin.readline())
print(solution(numbers, target))



# DFS
# answer = 0
# def DFS(idx, numbers, target, hop):
#     global answer
#     if idx+1 == len(numbers):
#         if hop == target:
#             answer += 1
#         return answer
#     DFS(idx+1, numbers, target, hop+numbers[idx+1])
#     DFS(idx+1, numbers, target, hop-numbers[idx+1])

# def solution(numbers, target):
#     # DFS
#     global answer
#     DFS(-1, numbers, target, 0)
#     return answer