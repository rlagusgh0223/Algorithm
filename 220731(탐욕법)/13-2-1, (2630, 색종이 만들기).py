import sys
n = int(sys.stdin.readline())

colorPaper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]    # 0과 1로 이루어진 종이의 상태 입력

white = 0
blue = 0

def dividedAndConquer(x, y, n):    # 분할정복을 위한 함수 좌표(x, y)와 크기 n을 받는다
    global blue, white    # 파란색 종이와 하얀색 종이의 수를 저장하기 위한 변수 생성
    sameColor=colorPaper[x][y]    # 해당 구역이 모두 같은 색인지 확인하기 위한 기준 변수 생성
    for i in range(x, x+n):
        for j in range(y, y+n):
            if sameColor != colorPaper[i][j]:    # 위에서 입력한 구분하기 위한 색과 다른 색이 있다면
                dividedAndConquer(x, y, n//2)    # 구역을 분할정복
                dividedAndConquer(x, y+n//2, n//2)
                dividedAndConquer(x+n//2, y, n//2)
                dividedAndConquer(x+n//2, y+n//2, n//2)
                return    # 함수 종료
    if sameColor==0:    # 위에서 종료되지 않았다면 이 구역을 모두 같은색인데 흰색이라면
        white += 1    # 하얀색 종이수 1 증가
        return
    else:    # 파란색이라면
        blue += 1    # 파란색 종이수 1 증가
        return

dividedAndConquer(0, 0, n)    # 분할정복 실행
print(white)
print(blue)