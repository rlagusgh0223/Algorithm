def solution(board, h, w):
    answer = 0
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    for i in range(4):
        hx, wy = h+dx[i], w+dy[i]
        if 0<=hx<len(board) and 0<=wy<len(board[0]):
            if board[h][w] == board[hx][wy]:
                answer += 1
    return answer

import sys
board = list(sys.stdin.readline().strip().split('"], ["'))
board = [now.split('", "') for now in board]
h, w = map(int, sys.stdin.readline().split())
print(solution(board, h, w))