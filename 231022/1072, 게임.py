import sys
X, Y = map(int, sys.stdin.readline().split())
Z = (Y*100) // X  # 이긴게임에 100을 곱하고 게임 횟수로 나누면 승률이 십의자리로 나온다
ans = -1  # Z가 변하지 않는다면 -1을 출력한다
left = 0
right = X
while left <= right:
    mid = (left+right) // 2  # Z를 올리기 위해 몇 판 더하는지 0부터 X판 중 필요한 수를 이진탐색으로 찾기 위한 변수
    if (Y+mid)*100 // (X+mid) > Z:  # mid번 게임을 더 했을때 승률이 Z보다 크다면 
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)