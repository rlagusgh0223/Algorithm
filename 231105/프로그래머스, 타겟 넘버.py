answer = 0
def DFS(idx, numbers, target, hop):
    global answer
    if idx+1 == len(numbers):
        if hop == target:
            answer += 1
        return answer
    DFS(idx+1, numbers, target, hop+numbers[idx+1])
    DFS(idx+1, numbers, target, hop-numbers[idx+1])

def solution(numbers, target):
    # DFS
    global answer
    DFS(-1, numbers, target, 0)
    return answer

    # BFS
    # answer = 0
    # q = deque()
    # q.append((numbers[0], 0))  # 지금까지 합한 값, 더한 위치
    # q.append((-1 * numbers[0], 0))
    # while q:
    #     hop, now = q.popleft()
    #     if hop==target and now==len(numbers)-1:
    #         answer += 1
    #     elif now+1 < len(numbers):
    #         q.append((hop+numbers[now+1], now+1))
    #         q.append((hop-numbers[now+1], now+1))
    # return answer

from collections import deque
import sys
numbers = list(map(int, sys.stdin.readline().split(", ")))
target = int(sys.stdin.readline())
print(solution(numbers, target))