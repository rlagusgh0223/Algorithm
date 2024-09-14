def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i%2 == 1:
            answer.append(strArr[i].upper())
        else:
            answer.append(strArr[i].lower())
    return answer

import sys

print(solution(list(sys.stdin.readline().strip().split('","'))))
