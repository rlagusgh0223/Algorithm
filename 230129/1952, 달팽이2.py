import sys
m, n = map(int, sys.stdin.readline().split())
board = [[1]*(n+2)] + [[1]+[0]*n+[1] for _ in range(m)] + [[1]*(n+2)]  # 사방을 1로 둘러싼 판 만들기
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
i = j = 1
dir = ans = 0
t = m*n
while True:
    if board[i][j] == 0:
        board[i][j] = 1
        i += di[dir]
        j += dj[dir]
        t -= 1
        if t == 0:
            print(ans)
            break
    else:
        i -= di[dir]
        j -= dj[dir]
        dir = (dir+1) % 4
        ans += 1
        i += di[dir]
        j += dj[dir]