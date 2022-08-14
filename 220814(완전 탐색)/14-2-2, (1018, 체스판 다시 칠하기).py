N, M = map(int, input().split())
chess = [list(x for x in input()) for _ in range(N)]
answer = []

for col in range(N-7):
    for row in range(M-7):
        countW = countB = 0
        for i in range(col, col+8):
            for j in range(row, row+8):
                if (i+j)%2==0:
                    if chess[i][j] != 'W':
                        countW += 1
                    if chess[i][j] != 'B':
                        countB += 1
                else:
                    if chess[i][j] !='W':
                        countB += 1
                    if chess[i][j] !='B':
                        countW += 1
        answer.append(min(countW, countB))
print(min(answer))