# 모범답안
# 이 방법으로는 파이썬은 시간초과 나온다
# 여기서 동적 프로그래밍 알고리즘을 추가로 사용해야 하며
# 그 코드는 나중에 배우면 다시 올리겠다
import sys

def recursive(y, x, shape):    # 파이프의 한쪽 끝 위치와 현재 파이프의 모양의 정보를 담고 있는 shape변수를 함수의 인자로 받는다
    global ans    # 정답을 저장하기 위한 변수
    if y>n or x>n:    # 파이프의 범위가 n보다 크다면 집의 범위를 넘었으므로 반환
        return
    if y==n and x==n:    # 파이프의 위치(y,x)가 판의 끝이라면 ans+=1로 정답을 1 증가시킨다
        ans += 1
    if home[y][x+1] == 0 and (shape==0 or shape==2):    # 파이프의 위치에서 오른쪽(x+1)으로 벽이 없고, 현재 모양이 가로(0) 혹은 대각선(2)이라면
        recursive(y, x+1, 0)    #  재귀함수 실행(y, x+1, 가로)
    if home[y+1][x] == 0 and (shape==1 or shape==2):    # 파이프의 위치에서 아래쪽(y+1)으로 벽이 없고, 현재 모양이 세로(1) 혹은 대각선(2)이라면
        recursive(y+1, x, 1)    # 재귀함수 실행(y+1, x, 세로)
    if home[y+1][x] == 0 and home[y][x+1] == 0 and home[y+1][x+1] == 0:    # 파이프의 위치에서 아래와 오른쪽, 대각선에 벽이 없으면
        recursive(y+1, x+1, 2)    # 재귀함수 실행(y+1, x+1, 대각선)

n = int(sys.stdin.readline())
home = [[0 for col in range(18)] for row in range(18)]
for i in range(1, n+1):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(1, n+1):
        home[i][j]=row[j-1]

ans = 0
recursive(1, 2, 0)
print(ans)