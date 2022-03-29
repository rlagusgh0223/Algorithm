import sys, copy
from unittest import result

array = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(4):
        array [i][j] = [data[j*2], data[j*2+1]-1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]    # 이 순서는 문제에서 주어진 대로 방향을 돌리기 위한 순서이므로 바꾸면 안된다
dy = [0, -1, -1, -1, 0, 1, 1, 1]
# dx = [-1, -1, -1, 0, 0, 1, 1, 1]    # 내가 외우기 쉬운 이 순서로 하면 방향이 틀려서 오답이 나온다
# dy = [-1, 0, 1, -1, 1, -1, 0, 1]

result = 0

#============================================
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None

def turn_left(direction):
    return (direction+1) % 8

def move_all_fishes(array, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                direction = turn_left(direction)
#============================================

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        if 0 <= now_x < 4 and 0 <= now_y < 4:
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def DFS(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)
    total += array[now_x][now_y][0]
    array[now_x][now_y][0] = -1
    move_all_fishes(array, now_x, now_y)#============================================
    positions = get_possible_positions(array, now_x, now_y)#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    if len(positions) == 0:
        result = max(result, total)
        return
    for next_x, next_y in positions:
        DFS(array, next_x, next_y, total)

DFS(array, 0, 0, 0)
print(result)