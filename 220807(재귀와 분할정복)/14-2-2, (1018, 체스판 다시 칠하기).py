n, m = map(int, input().split())    # n과 체스판의 상태 입력
board = []
answer = []

for _ in range(n):
    board.append(input())

for col in range(n-7):    # 세로 줄을 순회하기 위한 for문
    for row in range(m-7):    # 가로 줄을 순회하기 위한 for문. 8*8범위의 체스판을 탐색할 때 배열의 인덱스 범위를 넘지 않도록 n-7범위 사용
        countW = 0    # W부터 시작해서 다른 글자 수를 저장하기 위한 변수
        countB = 0    # B부터 시작해서 다른 글자 수를 저장하기 위한 변수
        for i in range(col, col+8):    # (col, row)부터 시작해서 8*8크기로 자른 체스판을 탐색한다
            for j in range(row, row+8):
                if (i+j)%2 == 0:
                    if board[i][j] != 'W':    # 해당 보드칸의 글자가 W와 다르다면 countW+=1
                        countW += 1
                    if board[i][j] != 'B':    # 해당 보드칸의 글자가 B와 다르다면 coutnB+=1
                        countB += 1
                else:
                    if board[i][j] != 'B':
                        countW += 1
                    if board[i][j] != 'W':
                        countB += 1
        answer.append(countW)
        answer.append(countB)

print(min(answer))