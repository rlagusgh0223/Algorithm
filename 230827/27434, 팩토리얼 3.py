# pypyt3로 돌리면 어쩔땐 시간초과 나고 어쩔땐 통과된다
import sys
N = int(sys.stdin.readline())
ans = 1
for i in range(N, 1, -1):
    ans *= i
print(ans)