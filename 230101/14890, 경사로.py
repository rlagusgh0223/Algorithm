def check(row):
    visited = [False] * n  # 각 위치에 대한 경사로 설치 여부
    for i in range(n-1):
        # 오른쪽 위치와 높이 차이가 2 이상인 경우, 불가능
        if abs(row[i] - row[i+1]) >= 2:
            return False
        # 높이 차이가 1인 경우
        if abs(row[i] - row[i+1]) == 1:
            # L개 만큼 확인하며
            for j in range(l):
                # 한 칸 내려가는 경우, 오른쪽으로 이동하며
                if row[i] - 1 == row[i+1]:
                    current = i + 1 + j
                    if current >= n:  # 공간을 벗어나는 경우
                        return False
                    if row[i+1] != row[current]:  # 높이가 다르다면
                        return False
                # 한 칸 올라가는 경우, 왼쪽으로 이동하며
                elif row[i] + 1 == row[i+1]:
                    current = i - j
                    if current < 0:  # 공간을 벗어나는 경우
                        return False
                    if row[i] != row[current]:  #높이가 다르다면
                        return False
                # 경사로가 이미 있다면, 지나가기 불가능
                if visited[current]:
                    return False
                visited[current] = True  # 경사로 설치하기
    return True

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
# 전체 N X N 맵 입력받기
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

answer = 0
for row in arr:  # 하나씩 행(row)을 확인하며
    if check(row):
        answer += 1
for i in range(n):  # 하나씩 열(column)을 확인하며
    column = []
    for j in range(n):
        column.append(arr[j][i])
    if check(column):
        answer += 1
print(answer)  # 지나갈 수 있는 길의 합