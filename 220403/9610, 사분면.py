import sys
n = int(sys.stdin.readline())
Q1 = Q2 = Q3 = Q4 = Q5 = AXIS = 0
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())    # 가로축(x)와 세로축(y) 입력
    if x > 0 and y > 0:    # 1사분면 좌표가 입력된 경우
        Q1 += 1
    elif x < 0 and y > 0:    # 2사분면 좌표가 입력된 경우
        Q2 += 1
    elif x < 0 and y < 0:    # 3사분면 좌표가 입력된 경우
        Q3 += 1
    elif x > 0 and y < 0:    # 4사분면 좌표가 입력된 경우
        Q4 += 1
    else:    # 그 외 나머지 경우, 즉 축에 있는 경우(x나 y가 0인 경우)
        AXIS += 1

print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)
print("Q4:", Q4)
print("AXIS:", AXIS)