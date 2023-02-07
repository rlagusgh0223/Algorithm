import sys
N = int(sys.stdin.readline())
condos = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
condos.sort()
cost = sys.maxsize
result = 0
for condo in condos:
    temp = condo[1]
    # 현재 콘도의 위치는 이전 콘도보다 머니까 이전 콘도까지의 최솟값보다 싸야한다
    if temp < cost:
        cost = temp
        result += 1
print(result)