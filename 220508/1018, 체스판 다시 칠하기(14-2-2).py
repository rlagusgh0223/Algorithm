import sys
N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
result = []

for col in range(N-7):    # 8*8 크기의 체스판을 제외하고 남는 길이
    for row in range(M-7):
        countW = 0    # W가 아닌 수 저장할 변수
        countB = 0    # B가 아닌 수 저장할 변수
        for i in range(col, col+8):    # 8 * 8크기의 체스판 탐색
            for j in range(row, row+8):
                if (i+j) % 2 == 0:    # 짝수칸의 문자. 첫 칸이랑 같아야 한다
                    if board[i][j] != 'W':    # W로 시작해서 W가 와야하지만 B가 온 경우
                        countW += 1
                    if board[i][j] != 'B':
                        countB += 1
                else:    # 홀수칸의 문자. 첫 칸이랑 달라야 한다
                    if board[i][j] != 'W':
                        countB += 1
                    if board[i][j] != 'B':    # W로 시작해서 B가 와야하지만 W가 온 경우
                        countW += 1
        result.append(min(countW, countB))    # 체스판의 면적 만큼 구했을때 더 적은 수를 입력한다
print(min(result))    # 체스판 검색 결과 중 가장 작은 값을 출력한다