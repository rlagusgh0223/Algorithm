# 가로, 세로를 0부터 시작해 자를 부분을 입력받은 후 정렬한다
# 가로, 세로 배열의 이전값~현재값의 크기를 구하고 가로*세로 중 가장 큰 값이 가장 큰 종이다
import sys
w, h = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
width = [0, w]
height = [0, h]
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x == 1:
        width.append(y)
    else:
        height.append(y)
width.sort()
height.sort()
result = 0
for i in range(1, len(width)):
    for j in range(1, len(height)):
        x = width[i] - width[i-1]
        y = height[j] - height[j-1]
        result = max(result, x*y)
print(result)