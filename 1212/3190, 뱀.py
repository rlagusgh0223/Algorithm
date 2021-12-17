from collections import deque
import sys

N = int(sys.stdin.readline())
board = [[0 for _ in range(N)] for _ in range(N)]

cnt1 = int(sys.stdin.readline())
for i in range(cnt1):
    x, y = map(int, sys.stdin.readline().split())
    board[x][y] = 1

cnt2 = int(sys.stdin.readline())
turn = [0] * cnt2
for i in range(cnt2):
    turn[i] = list(sys.stdin.readline().split())