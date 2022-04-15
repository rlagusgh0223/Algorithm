# 다이나믹 프로그래밍
from collections import deque
import sys

n = int(sys.stdin.readline())
tri = [0] * n
for i in range(n):
    tri[i] = list(map(int, sys.stdin.readline().split()))

# 다이나믹 프로그래밍으로 두번재 줄부터 내려가면서 확인
for i in range(1, n):
    for j in range(i+1):    # 한 줄에 하나씩 증가하니까 해당 중에 1개씩 더한 수 만큼 반복(ex. 1번줄은 3, 8 두개 있음)
        # 왼쪽 위에서 오는 경우
        if j == 0:          # 왼쪽에 올 숫자가 없는 경우 첫 수니까 기존값은 그냥 0이다
            up_left = 0
        else:               # 왼쪽에 받을 값이 있으면 up_left에 왼쪽에 있는 수를 입력한다
            up_left = tri[i-1][j-1]
        # 오른쪽 위에서 오는 경우(리스트 상으로는 바로 위)
        if j == i:          # 오른쪽에 올 숫자가 없는 경우
            up_right = 0
        else:               # 오른쪽에 받을 값이 있으면 up_right에 받는다(리스트상으로는 위에 있는 수니까 줄만 줄이고 열은 그대로 입력해서 받는다)
            up_right = tri[i-1][j]
        # 최대 합을 저장
        tri[i][j] = tri[i][j] + max(up_left, up_right)  # 지금 값과 위에서 받을 값 중 최댓값을 더해서 현재 자리에서 낼 수 있는 최대 값을 만든다

print(max(tri[n-1]))        # 맨 마지막 줄에는 위에서부터 최댓값을 더한 각 줄의 최댓값이 있다 이 중 가장 큰 값 호출