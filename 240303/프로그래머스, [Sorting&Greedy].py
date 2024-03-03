def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[1])
    end = routes[0][1]
    for route in routes:
        if route[0] > end:
            answer += 1
            end = route[1]
    return answer

import sys

routes = list(sys.stdin.readline().strip().split("], ["))
routes = [list(map(int, route.split(","))) for route in routes]
print(solution(routes))