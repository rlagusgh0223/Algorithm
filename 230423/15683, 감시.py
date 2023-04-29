def fill(board, mode, x, y):  # 감시
    for i in mode:  # cctv 방향에 따라 탐색
        nx, ny = x, y  # 같은 방향을 그래프 끝까지 감시
        while True:
            nx, ny = nx+dx[i], ny+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 6:
                    break
                elif board[nx][ny] == 0:
                    board[nx][ny] = -1
            else:  # 범위를 넘어가면 중단
                break

def dfs(depth, board):  # 탐색
    global min_value  # 사각지대
    if depth == len(cctv):  # 모든 cctv 탐색 완료
        cnt = 0
        for i in range(n):
            cnt += board[i].count(0)
        min_value = min(min_value, cnt)
        return
    temp = copy.deepcopy(board)  # 보드 복제
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:  # cctv의 종류에 따른 방향에 따라
        fill(temp, i, x, y)  # 감시 시작
        dfs(depth+1, temp)  # 재귀호출
        temp = copy.deepcopy(board)  # 보드 초기화

import copy
n, m = map(int, input().split())
cctv = []  # cctv종류, x좌표, y좌표
board = []  # 사무실 정보
# cctv 방향 정보
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

# 북-동-=남-서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    for j in range(m):
        if 1 <= data[j] <= 5:
            cctv.append([data[j], i, j])

min_value = 100  # 사각지대, 가로세로 8 이하이므로 64칸을 넘지 못한다
dfs(0, board)
print(min_value)