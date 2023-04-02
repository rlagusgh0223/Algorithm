# 단순히 한 줄에 빈 칸이 두개 이상만 있으면 누울자리가 하나인게 아니라
# X로 한 줄이 나뉘더라도 나뉜 공간이 각각 2칸이 넘으면 전부 누울자리로 계산한다

import sys
N = int(sys.stdin.readline())
room = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
row, col = 0, 0
for i in range(N):
    rcnt, ccnt = 0, 0
    for j in range(N):
        if room[i][j] == '.':
            rcnt += 1
            if j==N-1:
                if rcnt>=2:
                    row += 1
                rcnt = 0
        elif room[i][j]=='X':
            if rcnt>=2:
                row += 1
            rcnt = 0
        if room[j][i] == '.':
            ccnt += 1
            if j==N-1:
                if ccnt>=2:
                    col += 1
                ccnt = 0
        elif room[j][i]=='X':
            if ccnt>=2:
                col += 1
            ccnt = 0
print(row, col)