import sys
A, B, C = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
ans = [0] * N
for i in range(N):
    for _ in range(3):
        a, b, c = map(int, sys.stdin.readline().split())
        ans[i] += A*a + B*b + C*c
print(max(ans))