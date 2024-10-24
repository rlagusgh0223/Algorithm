def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i + j <= k:
                answer += board[i][j]
    return answer

import sys

board = list(sys.stdin.readline().strip().split("],["))
board = [list(map(int, b.split(", "))) for b in board]
k = int(sys.stdin.readline())
print(solution(board, k))