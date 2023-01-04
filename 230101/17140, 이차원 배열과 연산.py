# 하나의 행(row)에 대하여 정렬을 수행하는 함수
def sort_row(row):
    counter = dict()  # 원소의 개수를 세는 카운터
    for x in row:
        if x == 0:  # 0은 무시
            continue
        if x not in counter:
            counter[x] = 1
        else:
            counter[x] += 1
    # 정렬 기준 : 1. 수의 등장 횟수가 커지는 순, 2. 수가 커지는 순
    sorted_counter = sorted(counter.items(), key=lambda x:(x[1], x[0]))
    # 정렬된 결과를 배열에 넣을 때는 (수, 등장 횟수)를 넣기
    result = []
    for val, cnt in sorted_counter:
        result += [val, cnt]
    return result

# 전치 행렬을 구하는 함수
def transpose(matrix):
    row_length = len(matrix)  # 행(row)의 길이
    column_length = len(matrix[0])  # 열(column)의 길이
    # 전치 행렬 만들기
    result = [[0]*row_length for i in range(column_length)]
    # 전치 행렬에 값 채워넣기
    for i in range(column_length):
        for j in range(row_length):
            result[i][j] = matrix[j][i]
    return result

import sys
# 빠른 입력 함수 이용
input = sys.stdin.readline

# 매초마다 배열에 대한 연산을 처리하는 함수
def process(matrix, operator):
    if operator == 'C':  # C 연산인 경우
        matrix = transpose(matrix)
    max_length = 0
    # 각 행을 기준으로 정렬 수행
    for i in range(len(matrix)):
        matrix[i] = sort_row(matrix[i])
        # 가장 긴 행 계산하기
        max_length = max(max_length, len(matrix[i]))
    # 가장 긴 행보다 짧은 행들은 0을 채우기
    for i in range(len(matrix)):
        gap = max_length - len(matrix[i])
        matrix[i] += [0] * gap
        # 길이가 100을 넘어가지 않도록 자르기
        matrix[i] = matrix[i][:100]
    if operator == 'C':  # 연산인 경우
        matrix = transpose(matrix)
    return matrix

# 3 X 3 배열(matrix) 및 r, c, k 입력받기
r, c, k = map(int, input().split())
matrix = []
for i in range(3):
    matrix.append(list(map(int, input().split())))

t = 0
while True:
    row_length = len(matrix)
    column_length = len(matrix[0])
    # 범위를 벗어나지 않으며
    if row_length>=r and column_length>=c:
        # matrix[r][c]의 값이 k일 때 종료
        if matrix[r-1][c-1] == k:
            print(t)
            break
    # 100초가 경과한 경우 종료
    if t == 100:
        print(-1)
        break
    # R 연산 혹은 C 연산 수행
    if row_length >= column_length:
        matrix = process(matrix, 'R')
    else:
        matrix = process(matrix, 'C')
    t += 1  # 1초 증가