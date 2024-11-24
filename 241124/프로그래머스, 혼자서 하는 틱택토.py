def solution(board):
    def check(player):
        for i in range(3):
            # 가로 3개 다 같은 돌일때
            if all(player==board[i][j] for j in range(3)):
                return True
            # 세로 3개 다 같은 돌일때
            if all(player==board[j][i] for j in range(3)):
                return True
        # 왼쪽 상단에서 오른쪽 하단이 같은돌일때
        # 비교할게 3개뿐이라 그냥 반복문 안쓰고 해봤다. 혹시 길이가 더 짧은까봐. 근데 아니네
        if player==board[0][0]==board[1][1]==board[2][2]:
            return True
        # 오른쪽 상단에서 왼쪽 하단이 같은돌일때
        if all(player==board[i][2-i] for i in range(3)):
            return True
        return False

    o_cnt = sum(b.count('O') for b in board)
    x_cnt = sum(b.count('X') for b in board)
    
    if o_cnt>x_cnt+1 or o_cnt<x_cnt:
        return 0
    
    o_win = check('O')
    x_win = check('X')

    # 승자가 둘인 경우는 없다
    if o_win and x_win:
        return 0
    # 승자는 있지만 돌의 수가 맞지 않으면 안된다
    if o_win and o_cnt!=x_cnt+1:
        return 0
    if x_win and x_cnt!=o_cnt:
        return 0
    
    return 1

import sys

b = list(sys.stdin.readline().strip().split('", "'))
print(solution(b))