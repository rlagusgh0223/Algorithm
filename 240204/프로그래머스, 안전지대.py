def solution(board):
    answer = 0
    dx = [1, 0, -1, 0, -1, 1, -1, 1]
    dy = [0, 1, 0, -1, -1, 1, 1, -1]
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 1:
                for i in range(8):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny]!=1:
                        board[nx][ny] = 2
    
    for i in range(len(board)):
        answer += board[i].count(0)
    return answer

import sys

board = list(sys.stdin.readline().strip().split("], ["))
board = [list(map(int, b.split(", "))) for b in board]
print(solution(board))