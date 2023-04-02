import sys
mine = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
visit = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
cnt = 0
for x in range(5):
    for y in range(5):
        now = visit[x][y]
        cnt += 1
        # 빙고판에 내가 작성한 수 위치 비교
        for i in range(5):
            for j in range(5):
                if mine[i][j] == now:
                    mine[i][j] = 0
        bingo = 0
        # 가로
        for i in range(5):
            if mine[i].count(0) == 5:
                bingo += 1
        # 세로
        for i in range(5):
            ck = True
            for j in range(5):
                if mine[j][i] != 0:
                    ck = False
                    break
            if ck:
                bingo += 1
        # 대각선
        if mine[0][0]==mine[1][1]==mine[2][2]==mine[3][3]==mine[4][4]==0:
            bingo += 1
        if mine[4][0]==mine[3][1]==mine[2][2]==mine[1][3]==mine[0][4]==0:
            bingo += 1
        if bingo >= 3:
            print(cnt)
            exit()