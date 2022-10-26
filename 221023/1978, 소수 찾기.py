def is_prime(now):
    if now < 2:
        return False
    i = 2
    while i*i <= now:
        if now%i == 0:
            return False
        i += 1
    return True

import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
ans = 0
for now in lst:
    if is_prime(now):
        ans += 1
print(ans)