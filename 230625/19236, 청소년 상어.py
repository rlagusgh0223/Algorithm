# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환(공간, 상어 x좌표, 상어 y좌표)
def get_posibble_positions(array, now_x, now_y):
    positions = []  # 상어가 이동 가능한 범위 내의 물고기들 좌표 저장할 리스트
    dir = array[now_x][now_y][1]  # 상어의 방향을 먹은 물고기의 방향으로 바꾼다
    # 현재의 방향으로 계속 이동시키기
    for i in range(4):
        now_x, now_y = now_x+dx[dir], now_y+dy[dir]
        # 범위를 벗어나지 않는지 확인하며
        if 0<=now_x<4 and 0<=now_y<4:
            # 물고기가존재하는 경우
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions


# 현재 위치에서 45도 반시계 방향 회전
def turn_left(direction):
    return (direction+1) % 8


# 현재 배열에서 특정한 번호의 물고기 위치 찾기(공간, 물고기 번호)
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None


# 모든 물고기를 회전 및 이동시키는 함수(공간, 상어 x좌표, 상어 y좌표)
def move_all_fishes(array, now_x, now_y):
    # 1번부터 16번까지의 물고기를 차례대로(낮은 번호부터) 확인
    for i in range(1, 17):
        # 해당 물고기의 위치 찾기
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]  # 물고기 좌표
            dir = array[x][y][1]  # 물고기 방향
            # 해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            for j in range(8):
                nx, ny = x + dx[dir], y + dy[dir]
                # 해당 방향으로 이동이 가능하다면 이동시키기(공간 안이고 상어와 좌표가 겹치지 않는다면)
                if 0<=nx<4 and 0<=ny<4 and (nx!=now_x or ny!=now_y):
                    array[x][y][1] = dir  # 이동할 방향 저장
                    array[x][y], array[nx][ny] = array[nx][ny], array[x][y]  # 물고기 위치 바꾸기
                    break  # 바꿨으면 이번 물고기는 이동 끝
                dir = turn_left(dir)  # 물고기가 이동할 수 없다면 현재 방향에서 반시계 방향으로 45도 움직인다


# 모든 경우를 탐색하기 위한 DFS 함수(공간, 상어 x좌표, 상어 y좌표, 현재 좌표까지 물고기 합)
def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)  # 리스트를 통째로 복사

    total += array[now_x][now_y][0]  # 현재 위치의 물고기 먹기
    array[now_x][now_y][0] = -1  # 물고기를 먹었으므로 번호 값을 -1로 변환

    move_all_fishes(array, now_x, now_y)  # 전체 물고기 이동시키기

    # 이제 다시 상어가 이동할 차례이므로, 이동 가능한 위치 찾기
    positions = get_posibble_positions(array, now_x, now_y)
    # 이동할 수 있는 위치가 하나도 없다면 종료
    if len(positions) == 0:
        result = max(result, total)  # 최댓값 저장
        return
    # 모든 이동할 수 있는 위치로 재귀적으로 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)



import copy

# 4x4 크기의 정사각형에 존재하는 각 물고기의 번호(없으면 -1)와 방향 값을 담는 테이블
array = [[None]*4 for _ in range(4)]

result = 0  # 물고기 합의 최댓값

for i in range(4):
    data = list(map(int, input().split()))
    # 매 줄마다 4마리의 물고기를 하나씩 확인하며
    for j in range(4):
        # 각 위치마다 [물고기의 번호, 방향]을 저장(위에서 각 물고기의 번호, 방향을 한 줄에 줬으므로 *2로 구분한다)
        array[i][j] = [data[j*2], data[j*2+1] - 1]

# 8가지방향에 대한 정의(북쪽 1부터 순서대로)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 청소년 상어의 시작 위치(0, 0)에서부터 재귀적으로 모든 경우 탐색
dfs(array, 0, 0, 0)
print(result)