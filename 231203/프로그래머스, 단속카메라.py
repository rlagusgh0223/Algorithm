def solution(routes):
    answer = 0
    now = -30001  # 최소 30000이므로 그보다 1 작은30001로 초기값을 만든다
    routes.sort(key=lambda x:x[1])  # 진출 지점을 기준으로 정렬한다
    for route in routes:
        if now < route[0]:
            answer += 1
            now = route[1]
    return answer

import sys
routes = list(sys.stdin.readline().strip().split("], ["))
routes = [list(map(int, r.split(","))) for r in routes]
print(solution(routes))