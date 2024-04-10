def solution(arr):
    answer = []
    for i in range(len(arr)):
        # 조건문을 더 간단하게 할 수 도 있는데
        # 문제에서 주어진걸 그대로 조건문으로 반영했다
        if len(answer) == 0:
            answer.append(arr[i])
        elif answer[-1] == arr[i]:
            answer.pop()
        elif answer[-1]!=arr[i]:
            answer.append(arr[i])
    if len(answer) == 0:
        answer = [-1]
    return answer

import sys

print(solution(list(map(int, sys.stdin.readline().strip().split(", ")))))
