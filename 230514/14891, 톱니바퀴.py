# 회전하는 바퀴인지 확인하는 함수
def DFS(index, dir, rot, move):
    if index<3 and dir=='R':  # 오른쪽 바퀴가 비교할 수 있는 위치이고 오른쪽 바퀴를 비교하는 상황이라면
        if gears[index][2] != gears[index+1][6]:  # 두 바퀴의 극이 다를 경우 바퀴는 회전한다
            DFS(index+1, dir, rot*-1, True)  # 이동한 바퀴를 기준으로 그 다음 바퀴를 비교한다
    elif index>0 and dir=='L':  # 왼쪽 바퀴가 비교할 수 있는 위치이고 왼쪽 바퀴를 비교하는 상황이라면
        if gears[index-1][2] != gears[index][6]:  # 두 바퀴의 극이 다를 경우 바퀴는 회전한다
            DFS(index-1, dir, rot*-1, True)  # 이동한 바퀴를 기준으로 그 다음 바퀴를 비교한다
    if move:
        rotate(index, rot)

# 실질적으로 바퀴를 돌리는 함수
def rotate(index, rot):
    result = [0] * 8
    if rot == 1:  # 시계방향으로 돌아가는 경우
        for i in range(8):
            result[(i+1)%8] = gears[index][i]
    else:  # 반시계방향으로 돌아가는 경우
        for i in range(8):
            result[(i-1)%8] = gears[index][i]
    gears[index] = result

import sys
gears = [[] for _ in range(4)]
for i in range(4):
    gear = sys.stdin.readline().rstrip()
    for g in gear:
        gears[i].append(int(g))
K = int(sys.stdin.readline())
for _ in range(K):
    index, rot = map(int, sys.stdin.readline().split())
    index -= 1
    DFS(index, "R", rot, False)  # 여기서 True를 주면 이번과 밑에거로 인해 두 번 돌리게 된다
    DFS(index, "L", rot, True)
ans = 0
for i in range(4):
    if gears[i][0] == 1:
        ans += 2**i
print(ans)