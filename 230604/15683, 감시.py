# 이번 cctv가 감시할 수 있는 구역 체크
def check(room, mode, x, y):
    # cctv가 점검 가능한 방향 체크(ex [0, 2], [1, 2, 3])
    for i in mode:
        nx, ny = x, y
        while True:
            # 벽을 만나거나 사무실이 끝날때까지 반복
            nx, ny = nx+dx[i], ny+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if room[nx][ny] == 6:
                    break
                # cctv 감시 가능 구역은 다른 수로 변경하여 나중에 사각지대를 체크할때 체크되지 않게 한다
                elif room[nx][ny] == 0:
                    room[nx][ny] = -1
            else:
                break

def DFS(depth, room):
    global min_value
    # 모든 cctv의 범위를 체크했다면 사각지대를 확인한다
    if depth == len(cctv):
        cnt = 0
        for i in range(N):
            cnt += room[i].count(0)
        min_value = min(min_value, cnt)
        return
    # 모든 cctv가 감시할 수 있는 구역 체크
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        temp = copy.deepcopy(room)  # 원본은 건들지 않고 cctv감시 구역을 표시하기 위해 리스트 복사
        check(temp, i, x, y)
        DFS(depth+1, temp)

import sys, copy
N, M = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cctv = []  # cctv 종류, x좌표, y좌표
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]
for i in range(N):
    for j in range(M):
        if 1 <= room[i][j] <= 5:  # cctv는 cctv배열에 넣는다
            cctv.append([room[i][j], i, j])
min_value = 100  # 사각지대, 사무실은 최대 8칸이므로 사각지대는 64를 넘지 않는다
DFS(0, room)
print(min_value)