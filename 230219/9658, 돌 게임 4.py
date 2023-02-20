# 선공이 상근이이기 때문에 상근이가 판을 좀더 짤 수 있도록 유리하다
# 어떻게든 마지막에 자기가 안 가져가려고 할 것이다
# 마지막 돌에서 봤을때 i-1, i-3, i-4 중 하나라도 상근이가 가져간게 있다면
# 상근이는 마지막 돌을 피할 것이다
# 1 : 상근이 가져감, 0 : 창영이 가져감
import sys
N = int(sys.stdin.readline())
stone = [1, 0, 1, 0] + [0] * (N-4)
for i in range(4, N):
    if stone[i-1]==stone[i-3]==stone[i-4]==0:
        stone[i] = 1
if stone[N-1]:
    print("CY")
else:
    print("SK")