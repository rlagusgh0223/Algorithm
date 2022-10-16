import sys
W, H, X, Y, P = map(int, sys.stdin.readline().split())
cnt = 0
for i in range(P):
    x, y = map(int, sys.stdin.readline().split())
    if X<=x<=(X+W) and Y<=y<=(Y+H):
        cnt += 1
    else:
        R = H/2
        d1 = ((x-X)**2 + (y-(Y+R))**2)**0.5  # 왼쪽 반원 중심 좌표로부터 입력받은 좌표의 직선거리
        d2 = ((x-(X+W))**2 + (y-(Y+R))**2)**0.5  # 오른쪽 반원 중심 좌표로부터 입력받은 좌표의 직선거리
        if d1<=R or d2<=R:  # 원의 중심과 입력받은 좌표의 직선거리가 원의 반지름 안에 있다면 원 내부에 있으므로 cnt+=1
            cnt += 1

print(cnt)