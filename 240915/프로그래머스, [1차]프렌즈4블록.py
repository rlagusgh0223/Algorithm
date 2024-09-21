def solution(m, n, board):
    answer = 0
    ck = True  # 한 번 이라도 문자가 공백이 되지 않으면(블록이 사라지지 않은 경우) False
    board = [list(b) for b in board]  # 모든 문자열 리스트로 받기
    while ck:
        check = [[0]*n for _ in range(m)]
        ck = False

        # 현재 문자가 공백이 아니며
        # [i+1][j], [i][j+1], [i+1][j+1]이 같은 문자일 경우 체크 리스트에 체크한다
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == ' ':
                    continue
                elif board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    ck = True
                    check[i][j]=check[i+1][j]=check[i][j+1]=check[i+1][j+1]=1
        
        # 체크리스트에 체크된 문자들을 지운다
        for i in range(m):
            for j in range(n):
                if check[i][j] == 1:
                    board[i][j] = ' '
        #     print(board[i])
        # print()

        # 위에서부터 [i+1][j]의 문자가 비어있는 경우 위의 문자로 바꾼다
        for i in range(m-1, 0, -1):
            for j in range(n):
                if board[i][j] == ' ':
                    for k in range(i-1, -1, -1):
                        if board[k][j] != ' ':
                            board[i][j], board[k][j] = board[k][j], board[i][j]
                            break

        # 지워진 블록들의 수를 계산한다
        for i in range(m):
            answer += sum(check[i])
        #     print(board[i])
        # print('=====================')
    return answer

import sys

m, n = map(int, sys.stdin.readline().split())
board = list(sys.stdin.readline().strip().split('", "'))
print(solution(m, n, board))