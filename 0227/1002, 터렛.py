import sys, math
n = int(sys.stdin.readline())
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    r = math.sqrt((x1-x2)**2 + (y1-y2)**2)    # 두 원의 중심 사이의 거리
    
    if r == 0:    # 두 원의 중심이 같을 경우
        if r1 == r2:    # 두 원의 크기가 같아 겹치는 경우
            print('-1')
        else:    # 한 원이 다른 원 안에 들어가 있는 경우
            print('0')
    else:    # 두 원의 중심이 다를 경우
        if r1 + r2 == r or abs(r2 - r1) == r:    # 외접인 경우
            print('1')
        elif abs(r1-r2) < r < r1+r2:    # 두 반지름의 합은 중심거리보다 크고, 중심거리가 두 반지름의 차보다 큰 경우
            print('2')
        else:    # 외의의 경우는 모두 접점이 없으므로 0 출력
            print('0')