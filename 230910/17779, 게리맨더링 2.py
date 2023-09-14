import sys

def calculate(row, col, d1, d2):
    global total, answer
    first = second = third = fourth = 0

    # 구역1
    col1 = col + 1
    for r in range(row+d1):
        if r >= row:
            col1 -= 1
        first += sum(matrix[r][:col1])

    # 구역2
    col2 = col + 1
    for r in range(row+d2+1):
        if r > row:
            col2 += 1
        second += sum(matrix[r][col2:])
    
    # 구역3
    col3 = col - d1
    for r in range(row+d1, N):
        third += sum(matrix[r][:col3])
        if r < row+d1+d2:
            col3 += 1
    
    # 구역4
    col4 = (col+d2) - N
    for r in range(row+d2+1, N):
        fourth += sum(matrix[r][col4:])
        if r <= row+d1+d2:
            col4 -= 1
    
    # 구역5
    five = total - first - second - third - fourth
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
    total += sum(row)
answer = int(1e9)

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