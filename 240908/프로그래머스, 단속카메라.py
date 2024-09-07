def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    out = -30001
    for route in routes:
        if out < route[0]:
            answer += 1
            out = route[1]
    return answer

import sys

routes = list(sys.stdin.readline().strip().split("], ["))
routes = [list(map(int, r.split(","))) for r in routes]
print(solution(routes))