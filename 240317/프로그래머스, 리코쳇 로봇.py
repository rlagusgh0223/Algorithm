from collections import deque


def BFS(x, y, board):
    q = deque()
    q.append((x, y))
    # board는 str리스트인데 int로 값을 중간에 바꿀수 없다고 한다
    # 그러므로 board와 동일한 넓이의 int형 리스트로 방문했는지 체크해야 된다
    # 방문한 곳은 건너간 길이를 넣어준다
    visit = [[-1]*len(board[0]) for _ in range(len(board))]
    visit[x][y] = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x, y
            # 일반적인 BFS와는 다르게 판의 끝이나 D가 나올때까지 한번에 이동한다
            # 다음 칸에 이동 가능한지 먼저 확인한 후 값을 변경한다
            # 그래야 반복문을 나간 후 조건식에서 리스트 초과가 일어나지 않는다
            while 0<=nx+dx[i]<len(board) and 0<=ny+dy[i]<len(board[0]) and board[nx+dx[i]][ny+dy[i]]!='D':
                nx, ny = nx+dx[i], ny+dy[i]
            if board[nx][ny] == 'G':
                return visit[x][y] + 1
            if board[nx][ny]=='.' and visit[nx][ny]==-1:
                q.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1
    return -1

def solution(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                return BFS(i, j, board)

import sys

board = list(sys.stdin.readline().strip().split('", "'))
board = [list(now) for now in board]
print(solution(board))