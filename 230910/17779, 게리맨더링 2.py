import sys

def calculate(x, y, d1, d2):
    global total, answer
    first = second = third = fourth = 0

    # 구역1
    c1 = y + 1
    for r in range(x+d1):  # 1번 선거구 1 <= r < x+d1
        if r >= x:  # c의 구역을 계산하기 위한 조건문(1 <= c <= y)
            c1 -= 1  # 갈수록 1번 선거구의 y열 마지막은 작아진다
        first += sum(matrix[r][:c1])  # 1번 선거구의 값 더하기

    # 구역2
    c2 = y + 1
    for r in range(x+d2+1):  # 2번 선거구 1 <= r <= x+d2
        if r > x:  # c의 구역을 계산하기 위한 조건문(y < c <= N)
            c2 += 1  # 갈수록 y축 출발점을 뒤로 물린닫
        second += sum(matrix[r][c2:])
    
    # 구역3
    c3 = y - d1
    for r in range(x+d1, N):  # 3번 선거구(x+d1 <= r <= N)
        third += sum(matrix[r][:c3])
        if r < x+d1+d2:  # 밑으로 갈수록 끝 부분은 1구역씩 늘어난다
            c3 += 1
    
    # 구역4
    c4 = (y+d2) - N  # 얘는 무슨 원리인지 모르겠다...
    for r in range(x+d2+1, N):
        fourth += sum(matrix[r][c4:])
        if r <= x+d1+d2:  # 밑으로 갈수록 출발점은 1구역씩 줄어든다
            c4 -= 1
    
    # 구역5
    # total에서 1, 2, 3, 4 구역 뺀 값
    five = total - first - second - third - fourth
    
    # 기존에 있던 최솟값과 지금 나온 가장 많은 선거구와 가장 적은 선거구의 인구 차이 비교
    answer = min(answer, (max(first, second, third, fourth, five) - min(first, second, third, fourth, five)))

def check(x, y, d1, d2):  # 가능한 d1, d2 찾기
    # 경계선 구역
    # (x, y), (x+1, y-1), ..., (x+d1, y-d1)
    # (x, y), (x+1, y+1), ..., (x+d2, y+d2)
    # (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
    # (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
    if 0<=x+d1<N and 0<=x+d2<N and 0<=x+d1+d2<N:
        if 0<=y-d1<N and 0<=y+d2<N and 0<=y-d1+d2<=N:
            calculate(x, y, d1, d2)

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
total = 0
for row in matrix:
    total += sum(row)  # 현재 있는 모든 값의 합
answer = int(1e9)  # 출력할 최솟값 변수

# 기준점(x, y)의 행과 열은 d1, d2가 최소 1이므로
# 1 <= x < x+d1+d2 <= N
#   -> 1<=x<=N-2
# 1 <= y-d1 < y < y+d2 <= N
#   -> 2<=y<=N-1
for x in range(1, N-1):
    for y in range(2, N):
        for d1 in range(1, N-1):
            for d2 in range(1, N-1):
                check(x, y, d1, d2)
print(answer)