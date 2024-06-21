def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    rocks.append(distance)
    rocks.sort()
    while start <= end:
        mid = (start+end) // 2  # 가능한 최소 거리의 후보
        min_dis = distance+1  # 바위를 제거한 후 최소값을 저장할 변수
        now, remove = 0, 0  # 현재 위치, 제거한 바위의 수
        for rock in rocks:
            dis = rock - now  # 현재 위치에서 바위까지의 거리
            # 바위의 거리가 이번에 계산할 거리보다 작으면 바위를 제거한다
            if dis < mid:
                remove += 1
            # 바위의 거리가 mid와 같거나 크면
            # 바위의 거리가 가장 작은걸 입력하고, 현재 위치를 바위로 옮긴다
            else:
                min_dis = min(min_dis, dis)  # 유지된 바위들 사이의 최소거리 입력
                now = rock
        # 제거한 바위가 의도한 바위보다 많으면
        # 현재 mid의 값으로는 너무 많은 바위를 제거해야 하므로
        # 더 작은 값을 찾기 위해 end를 감소시킨다
        if remove > n:
            end = mid - 1
        # remove <= n인 경우,
        # 현재 mid값으로 바위들을 제거한 후의 최소거리
        # min_dis를 answer로 갱신한다
        # 가능한 더 큰 값을 찾기 위해 start를 증가시킨다
        else:
            start = mid + 1
            answer = min_dis
    return answer

import sys

distance = int(sys.stdin.readline())
rocks = list(map(int, sys.stdin.readline().split(", ")))
n = int(sys.stdin.readline())
print(solution(distance, rocks, n))