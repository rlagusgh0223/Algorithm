import sys
N = int(sys.stdin.readline())
cnt = 0
for _ in range(N):
    xi = sys.stdin.readline().rstrip()
    if int(xi[2:]) <= 90:
        cnt += 1
print(cnt)