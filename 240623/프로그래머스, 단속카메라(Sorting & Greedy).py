def solution(routes):
    answer = 0  # 필요한 단속용 카메라의 수를 저장할 변수
    routes.sort(key=lambda x:x[1])  # 진출 지점을 기준으로 오름차순 정렬
    check = -30001  # 카메라 위치(현재 차량의 진출지점)을 저장할 변수
    for r in routes:
        # 다음 차량이 현재 카메라의 위치(진출지점) 보다 크면
        if r[0] > check:
            # 카메라를 한 대 더 추가하고
            answer += 1
            # 그 카메라 위치를 현재 차량의 진출지점에 둔다
            check = r[1]
    return answer

import sys

routes = list(sys.stdin.readline().strip().split("], ["))
routes = [list(map(int, r.split(","))) for r in routes]
print(solution(routes))