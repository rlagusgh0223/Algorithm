import sys
input = sys.stdin.readline
n = int(input())
arr = [[False]*101 for _ in range(101)]

# 이 문제에서 x축과 y축은 일반적인 문제와 반대되는 의미를 자짐
# 0:우, 1:상, 2:좌, 3:하
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    x, y, d, g = map(int, input().split())  # 드래곤 커브의 시작점(x, y), 시작 방향(d), 세대(g)
    current = [d]  # 현재 이동 계획(current)
    for i in range(g):
        temp = []  # 현재 배열을 뒤집은 뒤에 1씩 더하여 temp 배열 생성
        for j in range(len(current)-1, -1, -1):
            temp.append((current[j]+1) % 4)
        current += temp  # temp 배열을 current 뒤에 붙이기
    # 드래곤 커브가 지나가는 점들
    arr[x][y] = True
    for i in range(len(current)):
        x = x + dx[current[i]]
        y = y + dy[current[i]]
        arr[x][y] = True

# 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수 계산
result = 0
for i in range(100):
    for j in range(100):
        if (arr[i][j] and arr[i][j+1] and arr[i+1][j] and arr[i+1][j+1]):
            result += 1
print(result)