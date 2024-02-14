def solution(array):
    answer = 0
    ck = []
    minA = 0
    for a in array:
        if a not in ck:
            ck.append(a)
            now = array.count(a)
            if minA == now:
                answer = -1
            if minA < now:
                answer = a
                minA = now
    return answer

import sys

array = list(map(int, sys.stdin.readline().split(", ")))
print(solution(array))