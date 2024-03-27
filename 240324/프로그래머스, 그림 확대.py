def solution(picture, k):
    answer = []
    for pic in picture:
        now = ''
        for p in pic:
            now += p*k
        for _ in range(k):
            answer.append(now)
    return answer

import sys

picture = list(sys.stdin.readline().strip().split('", "'))
k = int(sys.stdin.readline())
print(solution(picture, k))