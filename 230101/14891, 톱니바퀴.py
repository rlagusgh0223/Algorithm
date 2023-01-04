import sys
input = sys.stdin.readline

# 특정한 인덱스(index)의 톱니바퀴를 회전시키는 함수
# 연쇄 방향(direction) : 오른쪽(R) 혹은 왼쪽(L)으로 인접 톱니바퀴를 회전
def dfs(index, direction, rotation, move=True):
    # 오른쪽에 있는 톱니바퀴를 회전시키기
    if index<=2 and direction=='R':
        # 현재 기어의 오른쪽 극과 오른쪽 기어의 왼쪽 극이 다르다면
        if gears[index][2] != gears[index+1][6]:
            next_rotation = 'R'
            if rotation == 'R':
                next_rotation = 'L'
            dfs(index+1, 'R', next_rotation)
    # 왼쪽에 있는 톱니바퀴 회전시키기
    elif index>=1 and direction=='L':
        # 현재 기어의 왼쪽 극과 왼쪽 기어의 오른쪽 극이 다르다면
        if gears[index][6] != gears[index-1][2]:
            next_rotation = 'R'
            if rotation == 'R':
                next_rotation = 'L'
            dfs(index-1, 'L', next_rotation)
    # 최종적으로 내 톱니바퀴를 회전시키기
    if move:
        rotate(index, rotation)

# 4개의 톱니바퀴(gear) 정보 입력
gears = [[] for _ in range(4)]
for i in range(4):
    gear = input().strip()
    for j in range(len(gear)):
        gears[i].append(int(gear[j]))

# 한 톱니바퀴(index)를 시계방향(R) 혹은 반시계 방향(L)으로 회전
def rotate(index, rotation):
    result = [None] * 8
    # 톱니바퀴를 시계 방향으로 회전시키는 경우
    if rotation == 'R':
        for i in range(8):
            result[(i+1) % 8] = gears[index][i]
    # 톱니바퀴를 반시계 방향으로 회전시키는 경우
    if rotation == 'L':
        for i in range(8):
            result[(i-1) % 8] = gears[index][i]
    gears[index] = result

k = int(input())  # 회전할 톱니바퀴의 수
for i in range(k):
    index, rotation = map(int, input().split())
    index -= 1
    # 시계 방향 : R(1), 반시계 방향 : L(-1)
    if rotation == 1:
        rotation = 'R'
    else:
        rotation = 'L'
    # 시작 위치에서부터 오른쪽(R), 왼쪽(L)으로 인접한 톱니바퀴 회전
    dfs(index, 'R', rotation, move=False)
    dfs(index, 'L', rotation)  # 시작 톱니바퀴는 1번만 회전

# 최종 점수(score) 계산
result = 0
if gears[0][0] == 1:
    result += 1
if gears[1][0] == 1:
    result += 2
if gears[2][0] == 1:
    result += 4
if gears[3][0] == 1:
    result += 8
print(result)