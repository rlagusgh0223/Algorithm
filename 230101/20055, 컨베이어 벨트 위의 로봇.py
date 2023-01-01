from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
A = deque(map(int, sys.stdin.readline().split()))
B = deque([False] * N)
ans = 1
while True:
    # 1번
    A.rotate()
    B.rotate()
    B[N-1] = False
    # 2번
    for i in range(N-1, 0, -1):
        if not B[i] and B[i-1] and A[i]>0:
            B[i], B[i-1] = B[i-1], B[i]
            A[i] -= 1
    B[N-1] = False
    # 3번
    if A[0] > 0:
        A[0] -= 1
        B[0] = True
    # 4번
    if A.count(0) >= K:
        break
    ans += 1

print(ans)