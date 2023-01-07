# 1부터 시작한다고 했을때 SK와 CY가 갈 수 있는 위치
# SK : 1, 3
# CY : 2, 4, 6
# SK : 5, 7, 9
import sys
N = int(sys.stdin.readline())
if N%2 == 0:
    print("CY")
else:
    print("SK")