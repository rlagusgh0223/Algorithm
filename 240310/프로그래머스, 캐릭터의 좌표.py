def solution(keyinput, board):
    X, Y = board[0]//2, board[1]//2
    x, y = 0, 0
    for now in keyinput:
        if now=='up' and y+1<=Y:
            y += 1
        elif now=='down' and -Y<=y-1:
            y -= 1
        elif now=="left" and -X<=x-1:
            x -= 1
        elif now=='right' and x+1<=X:
            x += 1
    return [x, y]

import sys

keyinput = list(sys.stdin.readline().strip().split('", "'))
board = list(map(int, sys.stdin.readline().split(", ")))
print(solution(keyinput, board))