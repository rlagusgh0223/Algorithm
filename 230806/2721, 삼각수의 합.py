# n = 3이라면
# 1 * T(2) = 1 * (1 + 2) = 3
# 2 * T(3) = 2 * (1 + 2 + 3) = 12
# 3 * T(4) = 3 * (1 + 2 + 3 + 4) = 30
# 다 더해서 => 45

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    ans = sum(k * sum(range(1, k+2)) for k in range(1, n+1))
    print(ans)