def solution(arr):
    answer = max(arr)
    while True:
        check = True
        for now in arr:
            if answer%now != 0:
                answer += max(arr)
                check = False
                break
        if check:
            return answer

import sys
arr = list(map(int, sys.stdin.readline().split(',')))
print(solution(arr))