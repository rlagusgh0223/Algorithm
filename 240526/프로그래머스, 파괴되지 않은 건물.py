def solution(board, skill):
    answer = 0
    # 누적합을 할 리스트(행, 열 모두 누적합 해야된다)
    tmp = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]

    for t, r1, c1, r2, c2, d in skill:
        tmp[r1][c1] += d if t==2 else -d
        tmp[r1][c2+1] += d if t==1 else -d
        tmp[r2+1][c1] += d if t==1 else -d
        tmp[r2+1][c2+1] += d if t==2 else -d
    
    # 행 누적합 계산
    for i in range(len(tmp)-1):
        for j in range(len(tmp[i])-1):
            tmp[i+1][j] += tmp[i][j]
    
    # 열 누적합 계산
    for j in range(len(tmp[0])-1):
        for i in range(len(tmp)-1):
            tmp[i][j+1] += tmp[i][j]
    
    # board에 누적합 적용하고 파괴되지 않은 건물 계산
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += tmp[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer

import sys

board = list(sys.stdin.readline().strip().split("],["))
board = [list(map(int, b.split(","))) for b in board]
skill = list(sys.stdin.readline().strip().split("],["))
skill = [list(map(int, s.split(","))) for s in skill]
print(solution(board, skill))