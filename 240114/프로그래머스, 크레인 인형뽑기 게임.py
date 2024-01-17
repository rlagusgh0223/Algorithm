def solution(board, moves):
    answer = 0
    result = []
    for m in moves:
        m -= 1
        for i in range(len(board)):
            if board[i][m] != 0:
                if result and (result[-1] == board[i][m]):
                    del result[-1]
                    answer += 2
                else:
                    result.append(board[i][m])
                board[i][m] = 0
                break
    return answer


import sys
board = list(sys.stdin.readline().strip().split("],["))
for i in range(len(board)):
    board[i] = list(map(int, board[i].split(",")))
moves = list(map(int, sys.stdin.readline().split(",")))
print(solution(board, moves))