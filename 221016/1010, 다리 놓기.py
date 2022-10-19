# math의 comb 함수 이용
import sys
import math
T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(math.comb(M, N))