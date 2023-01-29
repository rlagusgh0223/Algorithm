# 이중 반복문을 이용해 x, y값을 따로 주면 53점이라고 한다
# y값만 반복문으로 주고 x값은 슬라이싱으로 줘야 맞다고 한다
import sys
N = int(sys.stdin.readline())
lst = [[0]*1001 for _ in range(1001)]
for now in range(N):
    x, y, r, c = map(int, sys.stdin.readline().split())
    for i in range(y, y+c):
        lst[i][x:x+r] = [now+1]*r
for cnt in range(1, N+1):
    result = 0
    for now in lst:
        result += now.count(cnt)
    print(result)