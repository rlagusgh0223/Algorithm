# N x M 초콜릿을 1 x M 초콜릿 N개로 나누기 위해 자르는 횟수는 N-1
# 1 x M 초콜릿을 1 x 1 초콜릿 M개로 나누기 위해 자르는 횟누는 M-1
# 즉, N x M 초콜릿을 1 x 1 초콜릿 N x M개로 나누기 위해 자르는 횟수는
# (N-1) + N x (M-1) = N - 1 + N x M - N = N x M - 1
import sys
N, M = map(int, sys.stdin.readline().split())
print(N * M - 1)