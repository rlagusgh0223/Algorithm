def solution(elements):
    answer = set()
    e = len(elements)
    elements = elements * 2
    for i in range(1, e+1):
        for j in range(e):
            answer.add(sum(elements[j:j+i]))
    return len(answer)

import sys
e = list(map(int, sys.stdin.readline().split()))
print(solution(e))