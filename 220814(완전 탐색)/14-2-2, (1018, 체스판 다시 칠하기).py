import sys
N, M = map(int, sys.stdin.readline().split())
chessboard = [[now for now in sys.stdin.readline().rstrip()] for _ in range(N)]
answer = []
for col in range(N-7):
    for row in range(M-7):
        countW = countB = 0
        for i in range(col, col+8):
            for j in range(row, row+8):
                if (i+j)%2==0:
                    if chessboard[i][j] != 'W':
                        countW += 1
                    else:
                        countB += 1
                else:
                    if chessboard[i][j] != 'W':
                        countB += 1
                    else:
                        countW += 1
        answer.append(min(countW, countB))
print(min(answer))