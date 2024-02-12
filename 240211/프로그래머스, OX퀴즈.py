def solution(quiz):
    answer = []
    quiz = [list(q.split()) for q in quiz]
    for q in quiz:
        x, y, z = int(q[0]), int(q[2]), int(q[4])
        if q[1] == '+':
            if x+y == z:
                answer.append("O")
            else:
                answer.append("X")
        if q[1] == '-':
            if x-y == z:
                answer.append("O")
            else:
                answer.append("X")
    return answer

import sys

q = list(sys.stdin.readline().strip().split('", "'))
print(solution(q))