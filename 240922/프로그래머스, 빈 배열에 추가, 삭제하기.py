def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        for j in range(arr[i]):
            if flag[i]:
                answer += [arr[i]] * 2
            else:
                del answer[-1]
    return answer

import sys

arr = list(map(int, sys.stdin.readline().split(", ")))
flag = [True if f=='true' else False for f in sys.stdin.readline().strip().split(", ")]
print(solution(arr, flag))