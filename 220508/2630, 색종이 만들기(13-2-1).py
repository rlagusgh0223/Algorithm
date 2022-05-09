# 모범답안
# 뭐라는지 모르겠다
# (0, 0) 이 주어졌을때 분할정복을 해야 된다면
# (0~n/2, 0~n/2)
# (n/2~n, 0~n/2)
# (0~n/2, n/2~n)
# (n/2~n, n/2~n)

import sys
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white = 0
blue = 0

def divideAndConquer(x, y, n):    # 현재 좌표와 해당 구역의 크기를 받는다
    global white, blue, cnt
    sameColor = paper[x][y]    # 해당 구역이 모두 같은 색인지 확인하기 위한 기준 변수 생성 / 현재 위치의 색 입력
    for i in range(x, x+n):    # 현재 좌표에서 해당 구역의 끝까지
        for j in range(y, y+n):
            if sameColor != paper[i][j]:    # 구역의 시작(sameColor)과 현재 좌표의 색(paper[i][j])이 다른 곳이 있다면
                divideAndConquer(x, y, n//2)
                divideAndConquer(x, y+n//2, n//2)
                divideAndConquer(x+n//2, y, n//2)
                divideAndConquer(x+n//2, y+n//2, n//2)
                return

    # 여기까지 왔다면 해당 구역은 모두 같은 색이다
    if sameColor == 0:    # 색이 흰 색이라면
        white += 1    # 하얀색 종이 수 1 증가
        return
    else:    # 색이 파란색이라면
        blue += 1    # 파란색 종이 수 1 증가
        return

divideAndConquer(0, 0, N)
print(white)
print(blue)