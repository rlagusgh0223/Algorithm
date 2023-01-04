# 하나의 행렬이 있을 때, 시계 방향으로 90도 회전시키는 함수
def rotate(matrix):
    n, m = len(matrix), len(matrix[0])
    result = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            result[i][j] = matrix[n-1-j][i]
    return result

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]

# N X N 행렬을 부분 격자들로 나누는 함수
def devide(l):
    step_size = 2**l
    positions = []
    for i in range(0, 2**n, step_size):
        for j in range(0, 2**n, step_size):
            positions.append(((i, j), (i+step_size, j+step_size)))
    return positions

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))  # DFS를 위한 재귀 제한 해제

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 맵의 크기 정보 N, 연산 횟수 Q 입력
n, q = map(int, input().split())
arr = []

# 행렬 입력
for i in range(2**n):
    row = list(map(int, input().split()))
    arr.append(row)

# 모든 연산 입력
operators = list(map(int, input().split()))

# 인접한 곳에 얼음이 없는 곳들을 녹이는 함수
def melt():
    melted = []
    for x in range(2**n):
        for y in range(2**n):
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 인접한 위치가 범위를 벗어나는 경우 무시
                if nx<0 or ny<0 or nx>=2**n or ny>=2**n:
                    continue
                # 인접한 위치에 얼음이 있는 경우 카운트
                if arr[nx][ny] >= 1:
                    cnt += 1
            # 주변에 얼음이 2개 이하로 있다면, 녹이기
            if cnt < 3:
                melted.append((x, y))
    return melted

# 하나씩 연산을 확인하며
for l in operators:
    # N X N 행렬을 부분 격자들로 나누기
    positions = devide(l)
    for position in positions:
        pos1, pos2 = position
        # 부분 격자 초기화
        current = []
        for i in range(pos1[0], pos2[0]):
            row = []
            for j in range(pos1[1], pos2[1]):
                row.append(arr[i][j])
            current.append(row)
        # 부분 격자 회전시키기
        current = rotate(current)
        # 회전된 결과 저장하기
        step_size = 2**l
        for i in range(step_size):
            for j in range(step_size):
                arr[i+pos1[0]][j+pos1[1]] = current[i][j]
    melted = melt()  # 녹일 위치 찾기
    for (x, y) in melted:  # 각 위치에 있는 얼음 녹이기
        if arr[x][y]>=1:
            arr[x][y] -= 1

# 모든 위치에 있는 얼음들의 합 출력
answer = 0
for row in arr:
    answer += sum(row)
print(answer)

# DFS를 위한 방문 처리 배열
visited = [[False]*(2**n) for _ in range(2**n)]

# DFS로 가장 큰 연결 요소 찾기
def dfs(x, y):
    result = 1  # 원소의 개수 세기
    for i in range(4):  # 인접한 위치 확인
        nx = x + dx[i]
        ny = y + dy[i]
        # 인접한 위치가 범위를 벗어나는 경우 무시
        if nx<0 or ny<0 or nx>=2**n or ny>=2**n:
            continue
        # 처음 방문하고, 얼음이 있는 곳에 대해서 세기
        if not visited[nx][ny] and arr[nx][ny]>=1:
            visited[nx][ny] = True  # 방문 처리
            result += dfs(nx, ny)
    return result

# 가장 큰 연결 요소의 크기 계산
max_value = 0
for i in range(2**n):
    for j in range(2**n):
        # 처음 방문하고, 얼음이 있으면(연결 요소) DFS 수행
        if not visited[i][j] and arr[i][j]>=1:
            visited[i][j] = True  # 방문 처리
            max_value = max(max_value, dfs(i,j))
print(max_value)