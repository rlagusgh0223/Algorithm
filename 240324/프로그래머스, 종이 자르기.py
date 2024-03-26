# 가로 M, 세로 N인 종이를 모두 길이 1인 사각형으로 만들기 위해서는
# M-1, N-1번 잘라야 한다
# 그러나 세로로 자를땐 이미 가로를 자른 다음이라고 가정하면
# M*(N-1)번 잘라야 한다
# 그러므로 계산식은 (M-1) + M*(N-1)이 나온다
# 이를 계산하면 MN - 1이 된다
def solution(M, N):
    return M*N - 1

import sys

M, N = map(int, sys.stdin.readline().split())
print(solution(M, N))