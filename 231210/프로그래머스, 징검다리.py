# 특정 최소거리를 기준으로 바위 사이의 거리가 그거보다 짧으면 지운다
# 그렇게 지운 바위의 갯수가 n개이면 거리의 최소 리턴
def solution(distance, rocks, n):
    answer = 0
    
    start, end = 0, distance
    rocks.append(distance)
    rocks.sort()
    while start <= end:
        mid = (start+end) // 2
        min_dis = distance + 1  # mid를 기준으로 돌을 제거했을때 돌 사이의 거리의 최솟값
        now, remove = 0, 0  # 현재 기준으로 삼은 돌의 위치, 제거한 돌의 갯수

        # 돌들의 거리와 mid 비교하여 제거할 돌의 갯수와 최소 거리 구하기
        for rock in rocks:
            dis = rock - now  # 현재 돌의 위치 - 기준으로 삼은 돌의 위치
            if dis < mid:  # 돌의 거리가 mid보다 짧으면 제거한다
                remove += 1
            else:  # 돌의 거리가 mid와 같거나 크면 최소거리 확인하고
                min_dis = min(min_dis, dis)
                now = rock  # 기준으로 삼은 돌의 위치를 현재 돌의 위치로 바꾼다

        # 제거한 돌의 갯수 비교하여 mid거리가 적당한지 확인
        if remove > n:  # 제거한 돌의 갯수가 n보다 많다면 
            end = mid - 1  # mid를 높게 잡은것이므로 end를 줄여준다
        else:# 그렇지 않다면 
            start = mid + 1  # mid를 낮게 잡은것이므로 start를 높여준다
            answer = min_dis  # mid와 n이 같은 경우 현재의 최소 거리를 저장한다

    return answer

import sys
distance = int(sys.stdin.readline())
rocks = list(map(int, sys.stdin.readline().split(", ")))
n = int(sys.stdin.readline())
print(solution(distance, rocks, n))