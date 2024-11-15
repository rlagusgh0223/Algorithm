def solution(strlist):
    answer = []
    for s in strlist:
        answer.append(len(list((s))))
    return answer

import sys

print(solution(list(sys.stdin.readline().strip().split('", "'))))
