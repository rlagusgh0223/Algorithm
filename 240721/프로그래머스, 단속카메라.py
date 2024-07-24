def solution(routes):
    answer = 0
    cam = -30001
    # 차가 빠져 나오는 곳을 기준으로 정렬
    routes.sort(key = lambda x:x[1])
    # 현재 카메라로 다음 차가 들어오는것도 잡지 못하면
    # 다음 차가 나가는 곳에 새로 카메라를 하나 설치한다
    # 그 차가 나가기 전에 들어오는 차는 따로 카메라 설치할 필요 없다
    for x, y in routes:
        if cam < x:
            answer += 1
            cam = y
    return answer

import sys

routes = list(sys.stdin.readline().strip().split("], ["))
routes = [list(map(int, r.split(","))) for r in routes]
print(solution(routes))