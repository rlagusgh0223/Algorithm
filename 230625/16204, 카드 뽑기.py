import sys
N, M, K = map(int, sys.stdin.readline().split())
Omax = min(M, K)  # 앞, 뒷장이 O인 최대 경우의 수
Xmax = min(N-M, N-K)  # 앞, 뒷장이 X인 최대 경우의 수
print(Omax + Xmax)