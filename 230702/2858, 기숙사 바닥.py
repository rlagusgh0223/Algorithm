import sys
R, B = map(int, sys.stdin.readline().split())
# L은 가로, W는 세로인데
# 빨간색의 개수는
# 위, 아래 가로줄 수와 같고(L*2)
# 좌, 우의 세로줄은 맨 위,아래의 벽돌 각 1개를 뺀 값과 같아야 된다(W-2)*2
# 벽돌은 가로, 세로 각 양쪽으로 2개씩 빼면 된다
# (L-2) * (W-2)
for L in range(R//2):
    for W in range(L+1):
        if (L*2+(W-2)*2 == R) and ((L-2)*(W-2)==B):
            print(L, W)