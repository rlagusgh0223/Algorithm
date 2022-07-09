from collections import deque

def direction_change(d, c):
    # 0은 위, 1은 오른쪽, 2는 아래쪽, 3은 왼쪽이다
    if c=='L':    # 뱀의 방향을 왼쪽으로 회전
        d = (d-1) % 4
    else:    # 뱀의 방향을 오른쪽으로 회전
        d = (d+1) % 4
    return d

N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
L = int(input())  # 뱀의 방향 변환 횟수
times = {}    # 방향 변환 정보를 받기 위한 딕셔너리
for i in range(L):
    X, C = input().split()
    times[int(X)] = C    # 몇 초 후 어디로 변환하는지 입력
dx = [0, 1, 0, -1]    # direction때문에 이거 순서 바뀌면 답 안나온다
dy = [-1, 0, 1, 0]    # 좌표가 밑에서부터 반시계 방향으로 가야된다

direction = 1    # 뱀의 현재 이동 방향. 오른쪽을 나타내기 위한 변수 생성
time = 1    # 게임이 진행된 시간을 저장하기 위한 변수
x, y = 0, 0    # 뱀 머리의 현재 위치 저장을 위한 변수 생성
snake = deque([[y, x]])    # 뱀의 꼬리 위치를 큐의 형식으로 저장하기 위해 큐를 사용한다
# 이동한 칸에 사과가 없다면 뱀의 마지막 부분인 꼬리를 제거해 두어야 한다
# 즉, 가장 먼저 삽입된 끝 부분을 지워야 된다
board[y][x] = 2    # 뱀이 존재하는 곳은  board값을 2로 설정한다

while True:
    x, y = x+dx[direction], y+dy[direction]    # 이동을 위해 머리를 다음칸에 위치시킨다
    if 0<=x<N and 0<=y<N and board[y][x] != 2:    # 벽 또는 자기 자신의 몸과 부딪히지 않는다면
        if not board[y][x] == 1:    # 이동한 칸에 사과가 없다면
            delY, delX = snake.popleft()    # 꼬리부분(맨처음 입력부분)을 지워준다
            board[delY][delX] = 0
        board[y][x] = 2    # 전진한 머리 위치는 2로 바꿔서 뱀이 존재하는 것을 나타낸다
        snake.append([y, x])    # 머리 위치는 큐에 넣는다
        if time in times.keys():
            direction = direction_change(direction, times[time])    # 시간이 지나 방향전환을 해야한다면 direction_chamge함수를 통해 바꾼다
        time += 1
    else:    # 벽 또는 자기 자신과 부딪힌다면 끝
        break

print(time)