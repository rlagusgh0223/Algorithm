# 최댓값은 어차피 하나이므로 밑에서부터 올라와서 큰 값끼리 더하며 된다
def solution(triangle):
    floor = len(triangle) - 1  # 각 층수를 입력할 변수
    while floor > 0:
        for i in range(floor):  # 각 층에서 끝까지 계산
            # 위층에는 위층 기준으로 왼쪽 대각선(현재줄 배열로는 동일한 i), 오른쪽 대각선(배열로는 i+1)
            # 큰 값을 더한다
            triangle[floor-1][i] += max(triangle[floor][i], triangle[floor][i+1])
        floor -= 1  # 이번층 계산 종료 후 위층으로 올라간다
    return triangle[0][0]

import sys

triangle = list(sys.stdin.readline().strip().split("], ["))
triangle = [list(map(int, t.split(", "))) for t in triangle]
print(solution(triangle))