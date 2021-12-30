# from collections import deque
# import sys

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# T = deque()
# S = deque()
# cnt = 0

# endFlag = True

# while endFlag:                              # 입력이 잘못될 경우 계속 반복
#     N = int(sys.stdin.readline())           # 복도의 크기 입력
#     graph = ['X'] * N                       # 복도의 내용 입력할 리스트
#     t = 0                                   # 선생님, 학생, 엄폐물 여부 입력할 변수
#     s = 0
#     x = 0

#     if 3 <= N <= 6:                         # 복도 크기 범위 넘어가는지 확인
#         for i in range(N):                  # 선생님, 학생, 엄폐물 입력
#             graph[i] = list(sys.stdin.readline().split())
#         for i in range(N):                  # 선생님, 학생, 빈 공간 계산 및 선생님 위치 큐에 입력
#             for j in range(N):
#                 if graph[i][j] == 'T':
#                     T.append([i,j])
#                     t += 1
#                 elif graph[i][j] == 'S':
#                     S.append([i,j])
#                     s += 1
#                 elif graph[i][j] == 'X':
#                     x += 1
#         if t <= 5 and s <= 30 and x >=3:    # 입력 가능한 숫자 만큼만 입력해야 계산 진행
#             endFlag = False
#         else:
#             print("입력수 오류")
#     else:
#         print("잘못된 입력")

# EndFlag = True
# for i in range(len(T)):                     # 선생님 바로 옆에 학생이 있으면 벽을 세워도 엄폐가 안되므로 그냥 끝
#     x, y = T[i]
#     for j in range(4):
#         nx = x + dx[j]
#         ny = y + dy[j]
#         if 0 <= nx < N and 0 <= ny < N:
#             if graph[nx][ny] == 'S':
#                 EndFlag = False
#                 break
#     if not EndFlag:
#         break
    
# if EndFlag:                                 # 선생님 바로 옆에 학생이 없다면
#     for i in T:
#         t1 = i[0]
#         t2 = i[1]
#         for j in S:
#             s1 = j[0]
#             s2 = j[1]
#             X = (t1 + s1) // 2              # 선생과 학생 x, y 좌표의 중간
#             Y = (t2 + s2) // 2
#             if t1 == s1 and graph[t1][Y] == 'X':        # x좌표가 같을 경우 y좌표의 중간에 벽을 설치. 단, 빈 공간일 경우에만
#                 graph[t1][Y] = 'O'
#                 cnt += 1
#             elif t2 == s2 and graph[X][t2] == 'X':      # y좌표가 같을 경우 y좌표의 중간에 벽을 설치. 단, 빈 공간일 경우에만
#                 graph[X][t2] = 'O'
#                 cnt += 1

# if cnt == 3 and EndFlag:        # 엄폐물 설치 횟수가 3회이거나 선생님과 학생이 붙어있지 않다면 yes
#     print('YES')
# else:                           # 아니면 no
#     print('NO')


###############################################################
# 모범답안
# 근데 정답이 안나오는데?
from itertools import combinations

n = int(input())    # 복도의 크기
board = []  # 복도 정보(n * n)
teachers = []    # 모든 선생님 위치 정보
spaces = []     # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teachers.append((i, j))
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i, j))

# 특정 방향으로 감시를 진행(학새 발견 : True, 미발견 : False)
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':  # 학생이 있는 경우
                return True
            if board[x][y] == 'O':  # 장애물이 있는 경우
                return False
            y -= 1

    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1

    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1

    # 아래쪽 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님의 위치를 하나씩 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False    # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장애물 설치해보기
    for x, y in data:
        board[x][y] == 'O'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        # 원하는 경우를 발견한 것임
        find = True
        break
    # 설치된 장애물을 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')