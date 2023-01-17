import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(4):
    now = 1
    for j in range(i, N+i-3):
        now *= A[j]
    n1 = A[(N+i-3) % N]
    n2 = A[(N+i-2) % N]
    n3 = A[(N+i-1) % N]
    now = now+n1+n2+n3
    if ans < now:
        ans = now
print(ans)