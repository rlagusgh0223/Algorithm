def solution(todo_list, finished):
    answer = []
    for i in range(len(finished)):
        if not finished[i]:
            answer.append(todo_list[i])
    return answer

import sys

to = list(sys.stdin.readline().strip().split('", "'))
fin = list(sys.stdin.readline().strip().split(", "))
fin = [f == 'true' for f in fin]
print(fin)
print(solution(to, fin))