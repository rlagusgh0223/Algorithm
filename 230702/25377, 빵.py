import sys
N = int(sys.stdin.readline())
ans = 1001  # A와 B는 1000이하이므로 1001 이상의 수는 나올 수 없다
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    if A <= B:
        ans = min(ans, B)
if ans == 1001:
    print(-1)
else:
    print(ans)