def solution(board):
    # 정사각형이니까 한 변의 길이만 구하면 된다
    answer = board[0][0]
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            # 지금 정사각형의 한 변일 수 있다면
            if board[i][j] == 1:
                # 지금까지 가능한 변의 길이 중 가장 작은 값에서 현재값을 추가한다
                board[i][j] = 1 + min(board[i-1][j-1], board[i-1][j], board[i][j-1])
                # 지금까지 변의 길이 중 가장 긴 값 저장
                answer = max(answer, board[i][j])
        print(board[i])
    return answer ** 2

import sys
board = list(sys.stdin.readline().strip().split('],['))
board = [list(map(int, now.split(','))) for now in board]
print(solution(board))