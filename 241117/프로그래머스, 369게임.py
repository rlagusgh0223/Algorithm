def solution(order):
    answer = 0
    order = list(str(order))
    for i in range(3, 10, 3):
        answer += order.count(str(i))
    return answer

import sys

print(solution(int(sys.stdin.readline())))
