import sys
N = int(sys.stdin.readline())    # 보드의 크기
K = int(sys.stdin.readline())    # 사과의 개수
board = [[0 for _ in range(N)] for _ in range(N)]

for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x][y] = 1

L = int(sys.stdin.readline())    # 방향 전환 횟수
for i in range(L):
    X, C = sys.stdin.readline().split()