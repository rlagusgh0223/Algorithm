# 파이썬은 버블정렬 pypy3로 해야되는 것 같다
import sys
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
for _ in range(N-1):
    for i in range(N-1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            ck = False
            K -= 1
            if K == 0:
                print(A[i], A[i+1])
                exit()
print("-1")